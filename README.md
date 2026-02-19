# Itch.io Articles & Collections Generator

Автоматична генерація SEO-оптимізованих landing pages та створення колекцій на itch.io.
Підтримує кілька **профілів генерації** — ігрові колекції та колекції квізів/тестів.

---

## Структура проекту

```
├── master_process.py          # Запускає весь процес (єдина точка входу)
├── app.py                     # Генерація HTML через OpenAI API
├── generate_tasks.py          # Генерує tasks.csv з games.txt (тільки для games)
├── process_collections.py     # Створення колекцій на itch.io
├── config_raw.py              # Генерує config.json з raw curl
├── itch_collection_manager.py # Модуль для роботи з itch.io API
│
├── profiles/                  # Профілі генерації
│   ├── games.py               # Ігрові колекції
│   └── quizzes.py             # Колекції квізів / тестів
│
├── games.txt                  # Список ігор (для профілю games)
├── tasks.csv                  # Згенерований список задач для games
├── quiz-task.csv              # Задачі для профілю quizzes (ведеться вручну)
├── itchioGames.txt            # Список ігор itch.io (author.itch.io/game-name)
├── keywords/keywords.csv      # База ключових слів (для профілю games)
│
├── output/                    # Згенеровані HTML файли
└── config.json                # Конфігурація для itch.io (не в git)
```

---

## Профілі

Система підтримує два профілі, які керують:
- промтом для AI
- affiliate посиланням і його логікою
- зображенням кнопки
- форматом вхідного файлу задач

| | `games` | `quizzes` |
|---|---|---|
| Файл задач | `tasks.csv` | `quiz-task.csv` |
| Keywords lookup | ✅ | ❌ |
| Affiliate domain | `app-portal.club` | `appcentralhub.net` |
| Кнопка | `download-button-1.png` | `b2c-button-3.jpeg` |
| Генерація tasks | через `generate_tasks.py` | вручну у CSV |

---

## Швидкий старт

```bash
# Ігрові колекції
python master_process.py --profile games

# Колекції квізів
python master_process.py --profile quizzes
```

---

## Детальний процес

### Профіль `games`

**Кроки автоматизації:**

1. `config_raw.py` → генерує `config.json`
2. `generate_tasks.py` → генерує `tasks.csv` з `games.txt`
3. `app.py --profile games` → генерує HTML
4. `process_collections.py` → створює колекції на itch.io

**Підготовка `games.txt`** — один рядок = одна гра:

```
MultiVersus
WWE 2K22
Pokemon Emerald
```

**Формат `tasks.csv`** (генерується автоматично):

```csv
keyword,game
multiversus download,MultiVersus
wwe 2k22 download,WWE 2K22
```

---

### Профіль `quizzes`

**Кроки автоматизації:**

1. `config_raw.py` → генерує `config.json`
2. _(пропускається)_ — `quiz-task.csv` ведеться вручну
3. `app.py --profile quizzes` → генерує HTML
4. `process_collections.py` → створює колекції на itch.io

**Формат `quiz-task.csv`** (заповнюється вручну):

```csv
Keyword,Item Code,Collection ID
anxiety assessment teens,jobliti-anxiety,7010963
quiz for friends,personalio-friendship,7010964
```

> `Collection ID` — опціонально. Якщо не заповнено, підставляється `000000`.
> Affiliate посилання: `https://appcentralhub.net/take-test?domain=itchio&item=jobliti-anxiety&alias=tchC-anxiety-assessment-teens&code=7010963&source=source`

---

## Налаштування itch.io (config.json)

### Спосіб 1 — автоматично через `config_raw.py`

1. Відкрийте itch.io в браузері та увійдіть
2. DevTools (F12) → Network → виконайте будь-яку дію (наприклад, додайте гру до колекції)
3. Знайдіть POST запит → **Copy as cURL**
4. Вставте curl у `config_raw.py` у змінну `raw_curl`, також вкажіть `csrf_token`
5. Запустіть:

```bash
python config_raw.py
```

### Спосіб 2 — вручну

```bash
cp config.json.example config.json
```

Заповніть `config.json`:
- `itchio_token` — токен авторизації
- `itchio` — session cookie
- `cf_clearance` — Cloudflare cookie
- `csrf_token` — CSRF токен

---

## Тестовий запуск (dry-run)

Перевірте що все працює без реальних запитів:

```bash
python process_collections.py --dry-run
```

Покаже скільки колекцій буде створено, назви та які HTML файли будуть використані.

---

## Результат

Після виконання колекції записуються у `collections_result.csv`:

```csv
keyword,collection_id,collection_url,status
anxiety assessment teens,7010963,https://itch.io/c/7010963/anxiety-assessment-teens,success
```

> Кожна колекція використовує окрему гру з `itchioGames.txt`. Якщо ігор менше ніж keywords — скрипт використовує ігри по колу.

---

## Вимоги

- Python 3.x
- OpenAI API ключ у `.env` файлі (`OPENAI_API_KEY=...`)
- Бібліотеки:

```bash
pip install openai markdown python-dotenv requests
```

---

## Безпека

⚠️ **Ніколи не комітьте `config.json` в git!** Він містить чутливі дані (cookies, токени).

Файл вже додано до `.gitignore`.
