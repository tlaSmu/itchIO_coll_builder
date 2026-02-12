import csv
import os
import random

def generate_tasks_from_games(games_file="games.txt", keywords_file="keywords/keywords.csv", output_file="tasks.csv"):
    """
    Reads a list of games from games_file, finds the best keywords for each game
    from keywords_file, and generates a tasks.csv file.
    
    For each game, selects the keyword with highest volume that contains 'download'.
    """
    
    # Read games list
    if not os.path.exists(games_file):
        print(f"Error: {games_file} not found.")
        return
    
    with open(games_file, 'r', encoding='utf-8') as f:
        games = [line.strip() for line in f if line.strip()]
    
    print(f"Found {len(games)} games in {games_file}")
    
    # Read keywords
    if not os.path.exists(keywords_file):
        print(f"Error: {keywords_file} not found.")
        return
    
    keywords_by_game = {}
    
    with open(keywords_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if 'Group' in row and 'Keyword' in row and 'Volume' in row:
                # Skip rows with None values
                if row['Group'] is None or row['Keyword'] is None or row['Volume'] is None:
                    continue
                
                group = row['Group'].strip()
                keyword = row['Keyword'].strip()
                
                # Skip empty values
                if not group or not keyword:
                    continue
                
                try:
                    volume = int(row['Volume'])
                except ValueError:
                    volume = 0
                
                if group not in keywords_by_game:
                    keywords_by_game[group] = []
                
                keywords_by_game[group].append({
                    'keyword': keyword,
                    'volume': volume
                })
    
    print(f"Loaded keywords for {len(keywords_by_game)} games")
    
    # Generate tasks
    tasks = []
    
    for game in games:
        # Try to find matching keywords (case-insensitive)
        matching_group = None
        for group in keywords_by_game.keys():
            if group.lower() == game.lower():
                matching_group = group
                break
        
        if not matching_group:
            print(f"Warning: No keywords found for game '{game}'")
            continue
        
        game_keywords = keywords_by_game[matching_group]
        
        # Filter keywords that contain 'download'
        download_keywords = [
            kw for kw in game_keywords 
            if 'download' in kw['keyword'].lower()
        ]
        
        if not download_keywords:
            # If no 'download' keywords, use all keywords
            download_keywords = game_keywords
        
        # Filter keywords with volume > 20
        high_volume_keywords = [
            kw for kw in download_keywords
            if kw['volume'] > 20
        ]
        
        if high_volume_keywords:
            # Pick random keyword from those with volume > 20
            random_kw = random.choice(high_volume_keywords)
            best_keyword = random_kw['keyword']
            volume = random_kw['volume']
        else:
            # No keywords with volume > 20, pick random from all
            random_kw = random.choice(download_keywords)
            best_keyword = random_kw['keyword']
            volume = random_kw['volume']
        
        tasks.append({
            'keyword': best_keyword,
            'game': matching_group
        })
        
        print(f"✓ {matching_group}: {best_keyword} (volume: {volume})")
    
    # Write tasks.csv
    if tasks:
        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['keyword', 'game'])
            writer.writeheader()
            writer.writerows(tasks)
        
        print(f"\n✅ Generated {output_file} with {len(tasks)} tasks")
    else:
        print("\n⚠️ No tasks generated")

if __name__ == "__main__":
    generate_tasks_from_games()
