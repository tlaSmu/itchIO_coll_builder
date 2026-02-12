# Itch.io Articles & Collections Generator

Автоматична генерація SEO-оптимізованих landing pages та створення колекцій на itch.io.

## Структура проекту

- `app.py` - генерація HTML сторінок через OpenAI API
- `generate_tasks.py` - створення tasks.csv з ключовими словами
- `itch_collection_manager.py` - модуль для роботи з itch.io API
- `process_collections.py` - автоматичне створення колекцій
- `games.txt` - список ігор для обробки
- `itchioGames.txt` - список ігор на itch.io (формат: author.itch.io/game-name)
- `tasks.csv` - згенерований список завдань (keyword + game)
- `keywords/keywords.csv` - база ключових слів
- `output/` - згенеровані HTML файли
- `config.json` - конфігурація для itch.io (не в git)

## Використання

### 1. Генерація tasks.csv

Створіть файл `games.txt` зі списком ігор (одна гра на рядок):

```
MultiVersus
WWE 2K22
Pokemon Emerald
```

Запустіть скрипт:

```bash
python3 generate_tasks.py
```

Це створить `tasks.csv` з випадковими ключовими словами (volume > 20) для кожної гри.

### 2. Генерація HTML сторінок

Після створення `tasks.csv`, запустіть основний скрипт:

```bash
python3 app.py
```

Скрипт:
- Читає завдання з `tasks.csv`
- Генерує контент через OpenAI API (gpt-5.2)
- Конвертує Markdown в HTML
- Додає кнопку завантаження
- Зберігає файли в `output/`

**Налаштування:** Скрипт використовує мультипоточність (5 потоків). Змініть `max_workers` в `app.py` для регулювання швидкості.

### 3. Створення колекцій на itch.io

#### 3.1. Налаштування конфігурації

Створіть `config.json` на основі `config.json.example`:

```bash
cp config.json.example config.json
```

Заповніть `config.json` вашими даними:
- `itchio_token` - токен авторизації
- `itchio` - session cookie
- `cf_clearance` - Cloudflare cookie
- `csrf_token` - CSRF токен

**Як отримати токени:**
1. Відкрийте itch.io в браузері та увійдіть
2. Відкрийте DevTools (F12) → Network
3. Виконайте будь-яку дію (наприклад, додайте гру до колекції)
4. Знайдіть POST запит та скопіюйте cookies і csrf_token

#### 3.2. Тестовий запуск (dry-run)

Перевірте що все працює без реальних запитів:

```bash
python3 process_collections.py --dry-run
```

Це покаже:
- Скільки колекцій буде створено
- Назви колекцій (відформатовані в Title Case)
- Які HTML файли будуть використані

#### 3.3. Створення колекцій

Запустіть скрипт:

```bash
python3 process_collections.py
```

Скрипт:
1. Читає `tasks.csv`
2. Для кожного keyword:
   - Створює колекцію з назвою у Title Case
   - Додає **унікальну гру** з `itchioGames.txt` (по порядку)
   - Оновлює опис колекції з відповідного HTML файлу
   - Робить затримки 2-5 сек між запитами
3. Зберігає результати в `collections_result.csv`

> [!NOTE]
> Кожна колекція використовує окрему гру з `itchioGames.txt`. Якщо ігор менше ніж keywords, скрипт використовує ігри по колу.

**Формат `collections_result.csv`:**
```csv
keyword,collection_id,collection_url,status
multiversus download,6974230,https://itch.io/c/6974230/multiversus-download,success
```

#### 3.4. Обробка помилок

При невалідних токенах:
```
⚠️ Токени застаріли. Оновіть config.json
```

При помилці створення колекції - скрипт пропускає її і продовжує з наступною.

## Вимоги

- Python 3.x
- OpenAI API ключ в `.env` файлі
- Бібліотеки: `openai`, `markdown`, `python-dotenv`, `requests`

```bash
pip install openai markdown python-dotenv requests
```

## Безпека

⚠️ **Ніколи не комітьте `config.json` в git!** Він містить чутливі дані.

Файл вже додано до `.gitignore`.
