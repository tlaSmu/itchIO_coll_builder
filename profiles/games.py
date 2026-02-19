"""
Profile: games
Генерація landing page для ігрових колекцій на itch.io.
"""
import csv
import os

# ─────────────────────────────────────────────
# КОНФІГУРАЦІЯ ПРОФІЛЮ
# ─────────────────────────────────────────────

TASKS_FILE = "tasks.csv"

USE_KEYWORDS = True  # Шукати ключові слова у keywords/keywords.csv

BUTTON_IMAGE_URL = "https://validating-system.github.io/check/src/download-button-1.png"

# ─────────────────────────────────────────────
# ПРОМТ
# ─────────────────────────────────────────────

PROMPT = """
**Role:** You are a Senior SEO Content Writer specializing in software distribution landing pages.

**Task:** Create a landing page text for the game with the main SEO keyword.

**Tone of Voice:** Professional, technical, and dry. Avoid emotional adjectives or "marketing hype." The goal is to make the page look like a reliable official repository so that the user feels safe but finds the text too tedious to read, encouraging them to click the "Download" button instead.
The game name must be in Title Case throughout the text and in seo keywords.

**Structure Requirements:**
1. **H1 Header:** Create a dynamic header using the [GAME NAME]. It must include the [KEYWORD] and an official-looking build identifier.
   - **Requirement:** Vary the format for each generation. Use patterns such as:
     * "[Game Name] (Official Build ID: v.[X.X.X]-STABLE)"
     * "[Game Name] Latest Build v.[X.X.X]"
     * "[Game Name] Stable Build v.[X.X.X]"
     * "[Game Name] Stable Version v.[X.X.X]"
     * "[Game Name] Get Stable Version v.[X.X.X]"
   - Substitute [X.X.X] with random version numbers. 
   - Ensure the keyword is naturally integrated into the header or placed immediately below it.
2. **Introduction:** - Two short, formal paragraphs describing the game (as a technical simulation/product).
   - One long, verbose, and "blurry" paragraph describing the complex technical process of downloading and initializing the client.
3. **Section "Technical Details":** Write a SEO-optimized block using terms like: "latest version setup," "secure installation," "system compatibility," and "OS architecture."
4. **Table Structure (Vertical Layout):** Create a Markdown table with TWO columns: "Category" and "Specification / Feature". 
List all data points vertically. The rows must include:
- System Requirements (Minimum)
- Recommended Specs
- Supported Languages
- Accessibility (Visual)
- Accessibility (Input)
- Network Requirements
Ensure each cell contains clear, bullet-point-style technical data.
5. **Section "Recent Events & Announcements":** A brief, dry update on server stability or community events.
6. **Section "About This Game":** Use H3 headers to describe: 
   - Interaction Mechanics (physics-based interactions).
   - Customization (character skins/models).
   - Environment (location details).
7. **Section "Recent Updates":** A dry list of 3-4 patch notes (e.g., "collision detection refined," "API handshake optimized").
8. **FAQ:** 3 technical questions and answers about safety, cross-play, and versioning.

**Formatting:** Use Markdown only. Bolding main keywords is allowed and main sense.
"""

# ─────────────────────────────────────────────
# ФУНКЦІЇ ПРОФІЛЮ
# ─────────────────────────────────────────────

def build_affiliate_link(item_name: str, **kwargs) -> str:
    """Будує affiliate посилання для гри."""
    return (
        f"https://app-portal.club/get?domain=itchio"
        f"&item={item_name}"
        f"&alias=itchC{item_name.replace(' ', '')}"
        f"&code=000000"
        f"&source=source"
    )


def build_user_input(item_name: str, keyword: str, keywords_str: str = "", **kwargs) -> str:
    """Формує user input для запиту до AI."""
    return f"""game: {item_name}
main SEO keyword for optimized: {keyword}
keywords: {keywords_str}
"""


def load_tasks(tasks_file: str) -> list:
    """Завантажує задачі з tasks.csv (формат: keyword, game)."""
    tasks = []
    if not os.path.exists(tasks_file):
        print(f"❌ Файл задач не знайдено: {tasks_file}")
        return tasks

    with open(tasks_file, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            keyword = (row.get('keyword') or '').strip()
            game = (row.get('game') or '').strip()
            if keyword and game:
                tasks.append({
                    'keyword': keyword,
                    'item_name': game,
                })

    return tasks
