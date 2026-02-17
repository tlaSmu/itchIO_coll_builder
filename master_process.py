#!/usr/bin/env python3
"""
Master Process Script

Об'єднує всі кроки автоматизації створення колекцій на itch.io:
1. config_raw.py -> Генерує config.json з raw curl
2. generate_tasks.py -> Генерує tasks.csv з games.txt
3. app.py -> Генерує HTML контент для кожного завдання
4. process_collections.py -> Створює колекції на itch.io
"""

import subprocess
import sys
import time
import os

def run_step(script_name, description):
    """Виконує python скрипт і перевіряє результат."""
    print("\n" + "=" * 60)
    print(f"🔄 КРОК: {description}")
    print(f"📄 Скрипт: {script_name}")
    print("=" * 60 + "\n")
    
    start_time = time.time()
    
    try:
        # Використовуємо поточний інтерпретатор python
        # check=True викине виключення якщо скрипт поверне помилку
        subprocess.run([sys.executable, script_name], check=True)
        
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

def check_files():
    """Перевіряє наявність критичних файлів."""
    required_files = [
        'config_raw.py',
        'games.txt',
        'generate_tasks.py',
        'app.py',
        'process_collections.py',
        'itchioGames.txt'
    ]
    
    missing = []
    for f in required_files:
        if not os.path.exists(f):
            missing.append(f)
    
    if missing:
        print("❌ ВІДСУТНІ ФАЙЛИ:")
        for f in missing:
            print(f"  - {f}")
        return False
    return True

def main():
    print("\n🚀 ЗАПУСК MASTER PROCESS")
    print("=" * 60)
    
    # 0. Перевірка файлів
    if not check_files():
        print("\n❌ Зупинка через відсутні файли.")
        sys.exit(1)
    
    # 1. Генерація конфігурації (config.json)
    if not run_step('config_raw.py', "Генерація конфігурації з curl"):
        print("\n⚠️ Не вдалося створити config.json. Перевірте config_raw.py")
        sys.exit(1)
        
    # 2. Генерація завдань (tasks.csv)
    if not run_step('generate_tasks.py', "Генерація завдань з games.txt"):
        print("\n⚠️ Не вдалося створити tasks.csv")
        sys.exit(1)
        
    # 3. Генерація контенту (HTML)
    if not run_step('app.py', "Генерація HTML контенту (OpenAI)"):
        print("\n⚠️ Не вдалося згенерувати контент")
        sys.exit(1)
        
    # 4. Створення колекцій (itch.io)
    if not run_step('process_collections.py', "Створення колекцій на itch.io"):
        print("\n⚠️ Процес створення колекцій завершився з помилкою")
        sys.exit(1)
        
    print("\n" + "=" * 60)
    print("🎉 ВСІ ПРОЦЕСИ УСПІШНО ЗАВЕРШЕНО!")
    print("=" * 60)

if __name__ == "__main__":
    main()
