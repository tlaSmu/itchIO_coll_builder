"""
Profile: quizzes
Генерація landing page для колекцій квізів/тестів на itch.io.
"""
import csv
import os

# ─────────────────────────────────────────────
# КОНФІГУРАЦІЯ ПРОФІЛЮ
# ─────────────────────────────────────────────

TASKS_FILE = "quiz-task.csv"

USE_KEYWORDS = False  # Не шукати ключові слова у keywords/keywords.csv

BUTTON_IMAGE_URL = "https://validating-system.github.io/check/src/b2c-button-3.jpeg"

# ─────────────────────────────────────────────
# ПРОМТ
# ─────────────────────────────────────────────

# TODO: Замінити на реальний промт для квізів
PROMPT = """
**Role:** Senior SEO Content Writer & Assessment Methodologist.

**Task:** Create a high-authority landing page for the [MAIN KEYWORD].

**Tone of Voice:** Clinical, professional, and slightly academic. The goal is to make the user believe they are using a precise diagnostic instrument.

**SEO Strategy & Keyword Density:**

* **Density:** The [MAIN KEYWORD] must appear exactly **4 to 6 times** in the body text.
* **Variability:** At least 2-3 of these occurrences should be part of a natural phrase (e.g., "start your [Main Keyword] online," "get the [Main Keyword] results in PDF," or "access this free [Main Keyword] tool").
* **LSI:** Use synonyms like "evaluation," "assessment," "screening," or "diagnostic" to avoid keyword stuffing.

**Structure Requirements:**

1. **H1 Header:** Create a **seamless, natural phrase** (No colons, no dashes). The [MAIN KEYWORD] must be integrated into a complete, human-readable sentence.
* **Patterns (Examples):** * "Take the official [Main Keyword] for free online in 2026"
* "Access your professional [Main Keyword] with instant results"
* "Complete the [Main Keyword] to evaluate your current standing"
* "Start the validated [Main Keyword] for a comprehensive report"




2. **Introduction:** - **Para 1:** Define the [MAIN KEYWORD] as a standardized metric. (First keyword mention here).
* **Para 2:** Describe the target audience and the necessity of this evaluation. (Second keyword mention here).
* **Para 3 (The "Buffer"):** A dense, technical explanation of "weighted scoring," "standard deviation in results," and "normative sampling." Use a phrase like "the [Main Keyword] methodology ensures accuracy" here.


3. **Section "Assessment Protocol":** Explain the "technical" steps of the test. Mention the possibility to "download the [Main Keyword] summary" or "access the [Main Keyword] interface."
4. **Table (Vertical Layout):** Markdown table with "Category" and "Assessment Detail".
* **Assessment ID:** (Random alphanumeric, e.g., TEST-992-X)
* **Access Mode:** Free / Online / PDF Export
* **Evaluation Metric:** (Specific to the keyword)
* **Response Format:** (Likert Scale / Multiple Choice)
* **Processing Time:** (Real-time / Instant)


5. **Section "Methodology & Reliability":** Dry text about how the tool minimizes "response bias" and "measurement error."
6. **Section "Core Evaluation Domains":** H3 headers describing what exactly is being measured. (e.g., "Cognitive Baseline," "Affective Indicators").
7. **Section "Updates & Maintenance":** 3-4 bullet points on "scoring algorithm optimization" and "database updates."
8. **FAQ:** 3 questions using **long-tail variations** of the key.
* *Example:* "Is there a [Main Keyword] for free?"
* *Example:* "Can I save my [Main Keyword] results as a PDF?"



**Formatting:** Use Markdown. **Bold** the [MAIN KEYWORD] every time it appears to ensure SEO visibility.
"""

# ─────────────────────────────────────────────
# ФУНКЦІЇ ПРОФІЛЮ
# ─────────────────────────────────────────────

def build_affiliate_link(keyword: str, item_code: str = "", collection_id: str = "000000", **kwargs) -> str:
    """
    Будує affiliate посилання для квізу.

    Приклад результату:
    https://appcentralhub.net/take-test?domain=itchio
        &item=jobliti-anxiety
        &alias=tchC-anxiety-assessment-teens
        &code=7010963
        &source=source
    """
    alias = "tchC-" + keyword.lower().replace(" ", "-")
    return (
        f"https://appcentralhub.net/take-test?domain=itchio"
        f"&item={item_code}"
        f"&alias={alias}"
        f"&code={collection_id}"
        f"&source=source"
    )


def build_user_input(item_name: str, keyword: str, **kwargs) -> str:
    """Формує user input для запиту до AI."""
    return f"""quiz topic: {item_name}
main SEO keyword: {keyword}
"""


def load_tasks(tasks_file: str) -> list:
    """
    Завантажує задачі з quiz-task.csv.

    Формат CSV:
        Keyword,Item Code[,Collection ID]

    Collection ID — опціональне поле.
    Якщо відсутнє, підставляється '000000'.
    """
    tasks = []
    if not os.path.exists(tasks_file):
        print(f"❌ Файл задач не знайдено: {tasks_file}")
        return tasks

    with open(tasks_file, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            keyword = (row.get('Keyword') or '').strip()
            item_code = (row.get('Item Code') or '').strip()
            collection_id = (row.get('Collection ID') or '000000').strip()

            if keyword and item_code:
                tasks.append({
                    'keyword': keyword,
                    'item_name': keyword,       # для квізів item_name = keyword
                    'item_code': item_code,
                    'collection_id': collection_id,
                })

    return tasks
