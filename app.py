import os
import dotenv
from openai import OpenAI
import markdown
import re
import csv
import random
import concurrent.futures

dotenv.load_dotenv()

def get_random_keywords(game_name, csv_path="keywords/keywords.csv"):
    """
    Reads keywords from a CSV file where the 'Group' matches the game_name.
    Returns a string of up to 5 random keywords.
    """
    candidate_keywords = []
    try:
        # Check if file exists to avoid immediate crash if path is wrong
        if not os.path.exists(csv_path):
            print(f"Warning: Keywords file not found at {csv_path}")
            return ""

        with open(csv_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            # Normalize game_name for comparison
            target_group = game_name.strip().lower()
            
            for row in reader:
                # Check if 'Group' column exists and skip None values
                if 'Group' in row and 'Keyword' in row:
                    if row['Group'] is None or row['Keyword'] is None:
                        continue
                    
                    group = row['Group'].strip()
                    keyword = row['Keyword'].strip()
                    
                    # Skip empty values
                    if not group or not keyword:
                        continue
                    
                    # Check if matches target game
                    if group.lower() == target_group:
                        candidate_keywords.append(keyword)
                    
    except Exception as e:
        print(f"{game_name} > Error reading keywords CSV: {e}")
        return ""

    if not candidate_keywords:
        print(f"{game_name} > No keywords found for game: {game_name}")
        return ""

    # Select 5 random keywords, or all if fewer than 5
    selected = random.sample(candidate_keywords, min(5, len(candidate_keywords)))
    return ", ".join(selected)

def create_game_landing_page(game_name, main_seo_key):
    """
    Generates a landing page for the specified game and SEO keyword.
    Converts the AI-generated Markdown to HTML, injects a download button,
    and saves the file to the 'output' directory.
    """
    
    # Calculate affiliate link dynamically
    aff_link = f"https://validating-system.github.io/check/?utm_source=itch.io&utm_medium=000000&utm_campaign={game_name.lower().replace(' ', '+')}"

    # Get random keywords
    keywords_str = get_random_keywords(game_name)
    print(f"{game_name} > Selected keywords: {keywords_str}")

    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    user_instructions = """
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

    user_input = f"""
game: {game_name}
main SEO keyword for optimized: {main_seo_key}
keywords: {keywords_str}
"""

    print(f"Generating content for: {game_name}...")
    response = client.responses.create(
        model="gpt-5.2",
        instructions=user_instructions,
        input=user_input,
    )
    
    print("Content generated. Processing HTML...")

    # 1. Convert Markdown to HTML
    html_content = markdown.markdown(response.output_text, extensions=['tables'])

    # 2. Add Styles and Button
    style = '''
<style>
    table {
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
    }

    td,
    th {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
    }

    tr:nth-child(even) {
        background-color: #dddddd;
    }
</style>
'''
    # html_content = style + html_content
    html_content = html_content

    download_button_html = f'''
<div style="text-align: center; margin: 20px 0;">
    <a href="{aff_link}" target="_blank">
        <img src="https://validating-system.github.io/check/src/download-button-1.png" alt="Download Now" style="max-width: 100%; height: auto;">
    </a>
</div>
'''

    # Insert image with link after the first paragraph
    final_html = re.sub(r'</p>', f'</p>{download_button_html}', html_content, count=1)

    # 3. Save to file
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    safe_filename = f"{main_seo_key}.html"
    output_path = os.path.join(output_folder, safe_filename)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"✅ HTML saved to: {output_path}")



def run_task(task):
    """
    Helper function to call create_game_landing_page with a tuple.
    """
    keyword, game_name = task
    try:
        create_game_landing_page(game_name, keyword)
    except Exception as e:
        print(f"Error processing {game_name}: {e}")

if __name__ == "__main__":
    tasks_file = "tasks.csv"
    tasks = []
    
    if os.path.exists(tasks_file):
        with open(tasks_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if 'keyword' in row and 'game' in row:
                    # Skip None or empty values
                    if row['keyword'] is None or row['game'] is None:
                        continue
                    
                    keyword = row['keyword'].strip()
                    game = row['game'].strip()
                    
                    if keyword and game:
                        tasks.append((keyword, game))
    else:
        print(f"Tasks file {tasks_file} not found.")
        exit(1)

    print(f"Found {len(tasks)} tasks.")
    
    # Use ThreadPoolExecutor for concurrent execution
    # Determine number of threads (e.g., 5 is safe for API rate limits)
    max_workers = 5 
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(run_task, tasks)
        
    print("All tasks completed.")