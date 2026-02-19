import os
import argparse
import importlib
import dotenv
from openai import OpenAI
import markdown
import re
import csv
import random
import concurrent.futures

dotenv.load_dotenv()

MODEL = "gpt-5.2"


def get_random_keywords(item_name, csv_path="keywords/keywords.csv"):
    """
    Читає ключові слова з CSV де 'Group' відповідає item_name.
    Повертає рядок з до 5 випадковими ключовими словами.
    Використовується тільки якщо profile.USE_KEYWORDS == True.
    """
    candidate_keywords: list[str] = []
    try:
        if not os.path.exists(csv_path):
            print(f"Warning: Keywords file not found at {csv_path}")
            return ""

        with open(csv_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            target_group = item_name.strip().lower()

            for row in reader:
                if 'Group' in row and 'Keyword' in row:
                    if row['Group'] is None or row['Keyword'] is None:
                        continue

                    group = row['Group'].strip()
                    keyword = row['Keyword'].strip()

                    if not group or not keyword:
                        continue

                    if group.lower() == target_group:
                        candidate_keywords.append(keyword)

    except Exception as e:
        print(f"{item_name} > Error reading keywords CSV: {e}")
        return ""

    if not candidate_keywords:
        print(f"{item_name} > No keywords found for: {item_name}")
        return ""

    selected = random.sample(candidate_keywords, min(5, len(candidate_keywords)))
    return ", ".join(selected)


def create_landing_page(item_name: str, keyword: str, profile, extra: dict = None):
    """
    Генерує landing page за налаштуваннями профілю.

    Args:
        item_name: назва гри або теми квізу
        keyword:   головний SEO ключ (також ім'я вихідного файлу)
        profile:   модуль профілю (profiles.games або profiles.quizzes)
        extra:     додаткові параметри (item_code, collection_id тощо)
    """
    if extra is None:
        extra = {}

    # 1. Affiliate посилання через профіль
    aff_link = profile.build_affiliate_link(keyword=keyword, item_name=item_name, **extra)

    # 2. Ключові слова (тільки якщо профіль їх потребує)
    keywords_str = ""
    if getattr(profile, 'USE_KEYWORDS', False):
        keywords_str = get_random_keywords(item_name)
        print(f"{item_name} > Selected keywords: {keywords_str}")

    # 3. Запит до AI
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    user_input = profile.build_user_input(
        item_name=item_name,
        keyword=keyword,
        keywords_str=keywords_str,
        **extra,
    )

    print(f"Generating content for: {item_name}...")
    response = client.responses.create(
        model=MODEL,
        instructions=profile.PROMPT,
        input=user_input,
    )
    print("Content generated. Processing HTML...")

    # 4. Markdown → HTML
    html_content = markdown.markdown(response.output_text, extensions=['tables'])

    # 5. Кнопка з affiliate посиланням
    download_button_html = f'''
<div style="text-align: center; margin: 20px 0;">
    <a href="{aff_link}" target="_blank">
        <img src="{profile.BUTTON_IMAGE_URL}" alt="Get Started" style="max-width: 100%; height: auto;">
    </a>
</div>
'''

    # Вставляємо кнопку після першого параграфа
    final_html = re.sub(r'</p>', f'</p>{download_button_html}', html_content, count=1)

    # 6. Зберігаємо файл
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    safe_filename = f"{keyword}.html"
    output_path = os.path.join(output_folder, safe_filename)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"✅ HTML saved to: {output_path}")


def run_task(args):
    """Обгортка для паралельного виконання через ThreadPoolExecutor."""
    task, profile = args
    try:
        extra = {k: v for k, v in task.items() if k not in ('keyword', 'item_name')}
        create_landing_page(task['item_name'], task['keyword'], profile, extra=extra)
    except Exception as e:
        print(f"Error processing {task.get('item_name', '?')}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Генерація HTML landing pages для itch.io колекцій")
    parser.add_argument('--profile', default='games', choices=['games', 'quizzes'],
                        help="Профіль генерації: games (за замовчуванням) або quizzes")
    args = parser.parse_args()

    # Завантажуємо профіль динамічно
    profile = importlib.import_module(f"profiles.{args.profile}")
    print(f"📦 Профіль: {args.profile}")

    # Завантажуємо задачі через профіль
    tasks = profile.load_tasks(profile.TASKS_FILE)

    if not tasks:
        print(f"❌ Не знайдено задач у {profile.TASKS_FILE}")
        exit(1)

    print(f"Found {len(tasks)} tasks.")

    max_workers = 5
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(run_task, [(task, profile) for task in tasks])

    print("All tasks completed.")