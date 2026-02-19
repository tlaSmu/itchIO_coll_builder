#!/usr/bin/env python3
"""
Master Process Script

Об'єднує всі кроки автоматизації створення колекцій на itch.io.

Використання:
    python master_process.py                  # профіль games (за замовчуванням)
    python master_process.py --profile games  # ігрові колекції
    python master_process.py --profile quizzes # колекції квізів

Кроки для профілю 'games':
    1. config_raw.py      → Генерує config.json з raw curl
    2. generate_tasks.py  → Генерує tasks.csv з games.txt
    3. app.py             → Генерує HTML контент
    4. process_collections.py → Створює колекції на itch.io

Кроки для профілю 'quizzes':
    1. config_raw.py      → Генерує config.json з raw curl
    2. (пропускається)    → quiz-task.csv вже готовий
    3. app.py             → Генерує HTML контент
    4. process_collections.py → Створює колекції на itch.io
"""

import subprocess
import sys
import time
import os
import argparse


def run_step(script_name, description, extra_args=None):
    """Виконує python скрипт і перевіряє результат."""
    print("\n" + "=" * 60)
    print(f"🔄 КРОК: {description}")
    print(f"📄 Скрипт: {script_name}")
    print("=" * 60 + "\n")

    start_time = time.time()
    cmd = [sys.executable, script_name] + (extra_args or [])

    try:
        subprocess.run(cmd, check=True)
        elapsed = time.time() - start_time
        print(f"\n✅ {script_name} успішно завершено за {elapsed:.2f} сек.")
        return True

    except subprocess.CalledProcessError as e:
        print(f"\n❌ ПОМИЛКА: Скрипт {script_name} завершився з кодом {e.returncode}")
        return False
    except FileNotFoundError:
        print(f"\n❌ ПОМИЛКА: Скрипт {script_name} не знайдено!")
        return False
    except Exception as e:
        print(f"\n❌ НЕПЕРЕДБАЧЕНА ПОМИЛКА: {e}")
        return False


def check_files(profile_name):
    """Перевіряє наявність критичних файлів залежно від профілю."""
    # Файли, потрібні завжди
    required_files = [
        'config_raw.py',
        'app.py',
        'process_collections.py',
        'itchioGames.txt',
    ]

    # Файли, специфічні для профілю
    if profile_name == 'games':
        required_files += ['games.txt', 'generate_tasks.py']
    elif profile_name == 'quizzes':
        required_files += ['quiz-task.csv']

    missing = [f for f in required_files if not os.path.exists(f)]

    if missing:
        print("❌ ВІДСУТНІ ФАЙЛИ:")
        for f in missing:
            print(f"  - {f}")
        return False
    return True


def main():
    parser = argparse.ArgumentParser(description="Master process для itch.io колекцій")
    parser.add_argument('--profile', default='games', choices=['games', 'quizzes'],
                        help="Профіль генерації: games (за замовчуванням) або quizzes")
    args = parser.parse_args()
    profile_name = args.profile

    print(f"\n🚀 ЗАПУСК MASTER PROCESS  |  профіль: {profile_name.upper()}")
    print("=" * 60)

    # 0. Перевірка файлів
    if not check_files(profile_name):
        print("\n❌ Зупинка через відсутні файли.")
        sys.exit(1)

    # 1. Генерація конфігурації (config.json) — завжди
    if not run_step('config_raw.py', "Генерація конфігурації з curl"):
        print("\n⚠️ Не вдалося створити config.json. Перевірте config_raw.py")
        sys.exit(1)

    # 2. Генерація tasks.csv — тільки для games
    if profile_name == 'games':
        if not run_step('generate_tasks.py', "Генерація завдань з games.txt"):
            print("\n⚠️ Не вдалося створити tasks.csv")
            sys.exit(1)
    else:
        print(f"\n⏭️  Пропускаємо generate_tasks.py (профіль '{profile_name}' використовує власний файл задач)")

    # 3. Генерація HTML контенту
    if not run_step('app.py', f"Генерація HTML контенту (профіль: {profile_name})",
                    extra_args=['--profile', profile_name]):
        print("\n⚠️ Не вдалося згенерувати контент")
        sys.exit(1)

    # 4. Створення колекцій на itch.io — завжди
    if not run_step('process_collections.py', "Створення колекцій на itch.io",
                    extra_args=['--profile', profile_name]):
        print("\n⚠️ Процес створення колекцій завершився з помилкою")
        sys.exit(1)

    print("\n" + "=" * 60)
    print("🎉 ВСІ ПРОЦЕСИ УСПІШНО ЗАВЕРШЕНО!")
    print("=" * 60)


if __name__ == "__main__":
    main()
