#!/usr/bin/env python3
"""
Process Collections Script

Створює колекції на itch.io на основі keywords з файлу задач.
Файл задач визначається профілем (--profile games або --profile quizzes).
"""

import csv
import os
import sys
import argparse
import importlib
from itch_collection_manager import (
    load_config,
    human_delay,
    format_collection_title,
    create_collection_with_game,
    update_collection_description,
    get_html_content
)


def read_tasks_csv(tasks_file, profile):
    """
    Читає файл задач через профіль та повертає список завдань.
    Делегує завантаження профілю — кожен профіль знає свій формат.

    Returns:
        list of dict: [{'keyword': '...', ...}, ...]
    """
    tasks = profile.load_tasks(tasks_file)
    if tasks:
        print(f"📋 Завантажено {len(tasks)} завдань з {tasks_file}")
    return tasks


def read_itch_games(games_file='itchioGames.txt'):
    """
    Читає список ігор з itchioGames.txt.
    
    Returns:
        list of str: URLs ігор
    """
    if not os.path.exists(games_file):
        print(f"❌ Файл {games_file} не знайдено!")
        return []
    
    try:
        with open(games_file, 'r', encoding='utf-8') as f:
            games = [line.strip() for line in f if line.strip()]
        
        print(f"🎮 Завантажено {len(games)} ігор з {games_file}")
        return games
    
    except Exception as e:
        print(f"❌ Помилка читання {games_file}: {e}")
        return []


def save_results(results, output_file='collections_result.csv'):
    """
    Зберігає результати в CSV файл.
    
    Args:
        results: list of dict з результатами
        output_file: шлях до вихідного файлу
    """
    try:
        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            fieldnames = ['keyword', 'collection_id', 'collection_url', 'status']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        
        print(f"\n💾 Результати збережено в {output_file}")
    
    except Exception as e:
        print(f"❌ Помилка збереження результатів: {e}")


def process_collections(profile, tasks_file, games_file='itchioGames.txt',
                       config_file='config.json', dry_run=False):
    """
    Головна функція обробки колекцій.

    Args:
        profile:    модуль профілю (profiles.games або profiles.quizzes)
        tasks_file: шлях до файлу задач (визначається профілем)
        games_file: шлях до itchioGames.txt
        config_file: шлях до config.json
        dry_run:    якщо True, не виконує реальні запити
    """
    print("=" * 60)
    print("🚀 Запуск процесу створення колекцій")
    print("=" * 60)
    
    # 1. Завантажити конфігурацію
    config = load_config(config_file)
    if not config:
        print("\n❌ Не вдалося завантажити конфігурацію. Зупинка.")
        return
    
    # 2. Прочитати файл задач через профіль
    tasks = read_tasks_csv(tasks_file, profile)
    if not tasks:
        print("\n❌ Немає завдань для обробки. Зупинка.")
        return
    
    # 3. Вибрати ігри з itchioGames.txt
    games = read_itch_games(games_file)
    if not games:
        print("\n❌ Немає ігор в itchioGames.txt. Зупинка.")
        return
    
    if len(games) < len(tasks):
        print(f"\n⚠️ УВАГА: Ігор ({len(games)}) менше ніж завдань ({len(tasks)})")
        print(f"⚠️ Деякі ігри будуть використані повторно")
    
    if dry_run:
        print("\n🔍 DRY RUN MODE - реальні запити не виконуються\n")
    
    # 4. Обробка кожного завдання
    results = []
    
    for i, task in enumerate(tasks, 1):
        keyword = task['keyword']
        # 'game' — ключ у games профілі, 'item_name' — у quizzes
        game_name = task.get('game', task.get('item_name', ''))
        
        # Вибираємо унікальну гру для кожної колекції
        # Якщо ігор менше ніж завдань, використовуємо по колу
        selected_game = games[(i - 1) % len(games)]
        
        print(f"\n{'=' * 60}")
        print(f"📦 Обробка {i}/{len(tasks)}: {keyword}")
        print(f"🎮 Гра: {selected_game}")
        print(f"{'=' * 60}")
        
        # a. Форматувати назву колекції
        collection_title = format_collection_title(keyword)
        print(f"📝 Назва колекції: {collection_title}")
        
        # b. Знайти HTML файл
        html_file = f"output/{keyword}.html"
        print(f"📄 Шукаємо HTML: {html_file}")
        
        if not os.path.exists(html_file):
            print(f"⚠️ HTML файл не знайдено, пропускаємо...")
            results.append({
                'keyword': keyword,
                'collection_id': '',
                'collection_url': '',
                'status': 'failed - no html'
            })
            continue
        
        # c. Прочитати HTML контент для перевірки
        html_content = get_html_content(html_file)
        if not html_content:
            print(f"⚠️ Не вдалося прочитати HTML, пропускаємо...")
            results.append({
                'keyword': keyword,
                'collection_id': '',
                'collection_url': '',
                'status': 'failed - read error'
            })
            continue
        
        print(f"✅ HTML завантажено ({len(html_content)} символів)")
        
        if dry_run:
            print(f"🔍 [DRY RUN] Створення колекції '{collection_title}' з грою {selected_game}")
            print(f"🔍 [DRY RUN] Оновлення опису колекції")
            results.append({
                'keyword': keyword,
                'collection_id': 'DRY_RUN',
                'collection_url': 'DRY_RUN',
                'status': 'dry_run'
            })
            continue
        
        # d. Створити колекцію з грою
        collection_id = create_collection_with_game(selected_game, collection_title, config)
        
        if not collection_id:
            print(f"❌ Не вдалося створити колекцію, пропускаємо...")
            results.append({
                'keyword': keyword,
                'collection_id': '',
                'collection_url': '',
                'status': 'failed - create error'
            })
            continue
        
        # e. Затримка
        human_delay()
        
        # f. Перечитати HTML з collection_id для заміни affiliate посилань
        html_content_with_id = get_html_content(html_file, collection_id)
        if not html_content_with_id:
            print(f"⚠️ Помилка при перечитуванні HTML з collection_id")
            html_content_with_id = html_content  # Використовуємо оригінальний
        
        # g. Оновити опис колекції
        success = update_collection_description(collection_id, collection_title, html_content_with_id, config)
        
        # g. Затримка
        human_delay()
        
        # h. Зберегти результат
        collection_url = f"https://itch.io/c/{collection_id}/{keyword.replace(' ', '-')}"
        
        results.append({
            'keyword': keyword,
            'collection_id': collection_id,
            'collection_url': collection_url,
            'status': 'success' if success else 'partial - no description'
        })
        
        print(f"✅ Колекція оброблена: {collection_url}")
    
    # 5. Зберегти результати
    if not dry_run:
        save_results(results, 'collections_result.csv')
    
    # Підсумок
    print("\n" + "=" * 60)
    print("📊 ПІДСУМОК")
    print("=" * 60)
    
    if dry_run:
        print(f"🔍 DRY RUN завершено")
        print(f"📦 Буде створено колекцій: {len(tasks)}")
        for task in tasks:
            print(f"  - {format_collection_title(task['keyword'])}")
    else:
        success_count = sum(1 for r in results if 'success' in r['status'])
        failed_count = len(results) - success_count
        
        print(f"✅ Успішно: {success_count}")
        print(f"❌ Помилки: {failed_count}")
        print(f"📊 Всього: {len(results)}")
    
    print("=" * 60)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Створення колекцій на itch.io')
    parser.add_argument('--profile', default='games', choices=['games', 'quizzes'],
                        help='Профіль: games (за замовчуванням) або quizzes')
    parser.add_argument('--games', default='itchioGames.txt', help='Шлях до itchioGames.txt')
    parser.add_argument('--config', default='config.json', help='Шлях до config.json')
    parser.add_argument('--dry-run', action='store_true', help='Тестовий режим без реальних запитів')

    args = parser.parse_args()

    profile = importlib.import_module(f"profiles.{args.profile}")
    print(f"📦 Профіль: {args.profile}")

    process_collections(
        profile=profile,
        tasks_file=profile.TASKS_FILE,
        games_file=args.games,
        config_file=args.config,
        dry_run=args.dry_run
    )
