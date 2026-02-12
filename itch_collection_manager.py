import json
import os
import time
import random
import requests
from urllib.parse import quote

def load_config(config_path='config.json'):
    """
    Завантажує конфігурацію з JSON файлу.
    
    Args:
        config_path: шлях до config.json
        
    Returns:
        dict з cookies, csrf_token, headers або None при помилці
    """
    if not os.path.exists(config_path):
        print(f"❌ Файл {config_path} не знайдено!")
        print(f"💡 Створіть {config_path} на основі {config_path}.example")
        return None
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        # Валідація структури
        if 'itchio' not in config:
            print("❌ Невірна структура config.json - відсутній розділ 'itchio'")
            return None
        
        itchio = config['itchio']
        required_keys = ['cookies', 'csrf_token', 'headers']
        
        for key in required_keys:
            if key not in itchio:
                print(f"❌ Невірна структура config.json - відсутній '{key}'")
                return None
        
        return itchio
    
    except json.JSONDecodeError as e:
        print(f"❌ Помилка парсингу JSON: {e}")
        return None
    except Exception as e:
        print(f"❌ Помилка читання config: {e}")
        return None


def human_delay(min_sec=15, max_sec=35):
    """
    Рандомна затримка для імітації поведінки людини.
    
    Args:
        min_sec: мінімальна затримка в секундах
        max_sec: максимальна затримка в секундах
    """
    delay = random.uniform(min_sec, max_sec)
    print(f"⏳ Затримка {delay:.2f} сек...")
    time.sleep(delay)


def format_collection_title(keyword):
    """
    Форматує назву колекції - кожне слово з великої літери.
    
    Args:
        keyword: ключове слово (наприклад, "multiversus download")
        
    Returns:
        Відформатована назва (наприклад, "Multiversus Download")
    """
    return keyword.title()


def create_collection_with_game(game_url, collection_title, config):
    """
    Створює нову колекцію та додає гру.
    
    Args:
        game_url: URL гри (формат: author.itch.io/game-name)
        collection_title: назва колекції
        config: конфігурація з load_config()
        
    Returns:
        collection_id (str) або None при помилці
    """
    # Формуємо URL для запиту
    full_url = f"https://{game_url}/add-to-collection"
    
    # Підготовка даних
    data = {
        'source': 'game',
        'csrf_token': config['csrf_token'],
        'add_to': 'new',
        'collection[title]': collection_title,
        'collection[blurb]': '',
    }
    
    # Підготовка headers
    headers = config['headers'].copy()
    headers['referer'] = f"https://{game_url}"
    headers['origin'] = f"https://{game_url.split('/')[0]}"
    
    try:
        print(f"📤 Створення колекції '{collection_title}' з грою {game_url}...")
        
        response = requests.post(
            full_url,
            cookies=config['cookies'],
            headers=headers,
            data=data,
            timeout=30
        )
        
        if response.status_code == 200:
            # Спроба витягти collection_id з відповіді
            try:
                result = response.json()
                
                # Перевіряємо чи успішно створено
                if result.get('success'):
                    # Витягуємо ID з URL: https://itch.io/c/6974660/multiversus-download
                    if 'url' in result:
                        import re
                        match = re.search(r'/c/(\d+)/', result['url'])
                        if match:
                            collection_id = match.group(1)
                            print(f"✅ Колекція створена! ID: {collection_id}")
                            print(f"🔗 URL: {result['url']}")
                            return collection_id
                    
                    # Fallback: якщо є поле collection_id
                    if 'collection_id' in result:
                        collection_id = str(result['collection_id'])
                        print(f"✅ Колекція створена! ID: {collection_id}")
                        return collection_id
                    
                    print(f"⚠️ Колекція створена, але не вдалося витягти ID")
                    print(f"Response: {response.text[:200]}")
                    return None
                else:
                    print(f"❌ Створення не успішне: {result}")
                    return None
            except:
                print(f"⚠️ Відповідь не є JSON. Response: {response.text[:200]}")
                return None
        else:
            print(f"❌ Помилка створення колекції: HTTP {response.status_code}")
            print(f"Response: {response.text[:200]}")
            
            # Перевірка на невалідні токени
            if response.status_code == 403 or 'csrf' in response.text.lower():
                print("⚠️ Токени застаріли. Оновіть config.json")
            
            return None
    
    except requests.exceptions.Timeout:
        print("❌ Timeout при створенні колекції")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Помилка запиту: {e}")
        return None


def update_collection_description(collection_id, title, description_html, config):
    """
    Оновлює опис колекції.
    
    Args:
        collection_id: ID колекції
        title: назва колекції
        description_html: HTML опис
        config: конфігурація з load_config()
        
    Returns:
        True при успіху, False при помилці
    """
    url = f"https://itch.io/collection/{collection_id}/edit"
    
    # URL-encode HTML контенту
    encoded_description = quote(description_html)
    
    # Формуємо data string (як в publishTextToCollection.py)
    data = (
        f"csrf_token={quote(config['csrf_token'])}"
        f"&collection[private_changed]=1"
        f"&collection[on_profile_changed]=1"
        f"&collection[title]={quote(title)}"
        f"&collection[layout]=list"
        f"&collection[description]={encoded_description}"
    )
    
    headers = config['headers'].copy()
    headers['referer'] = url
    headers['origin'] = 'https://itch.io'
    
    try:
        print(f"📝 Оновлення опису колекції {collection_id}...")
        
        response = requests.post(
            url,
            cookies=config['cookies'],
            headers=headers,
            data=data,
            timeout=30
        )
        
        if response.status_code == 200:
            print(f"✅ Опис колекції оновлено!")
            return True
        else:
            print(f"❌ Помилка оновлення опису: HTTP {response.status_code}")
            print(f"Response: {response.text[:200]}")
            
            if response.status_code == 403 or 'csrf' in response.text.lower():
                print("⚠️ Токени застаріли. Оновіть config.json")
            
            return False
    
    except requests.exceptions.Timeout:
        print("❌ Timeout при оновленні опису")
        return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Помилка запиту: {e}")
        return False


def get_html_content(html_file_path, collection_id=None):
    """
    Читає HTML файл та повертає контент.
    Замінює utm_medium=000000 на utm_medium={collection_id} якщо передано collection_id.
    
    Args:
        html_file_path: шлях до HTML файлу
        collection_id: ID колекції для заміни в affiliate посиланнях
        
    Returns:
        HTML string або None при помилці
    """
    if not os.path.exists(html_file_path):
        print(f"❌ HTML файл не знайдено: {html_file_path}")
        return None
    
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Якщо передано collection_id, замінюємо 000000 на реальний ID
        if collection_id:
            content = content.replace('utm_medium=000000', f'utm_medium={collection_id}')
            print(f"🔗 Замінено affiliate ID: 000000 → {collection_id}")
        
        return content
    
    except Exception as e:
        print(f"❌ Помилка читання HTML: {e}")
        return None


if __name__ == "__main__":
    # Тестування функцій
    print("=== Тест format_collection_title ===")
    print(format_collection_title("multiversus download"))
    print(format_collection_title("wwe 2022 download"))
    
    print("\n=== Тест load_config ===")
    config = load_config('config.json')
    if config:
        print("✅ Конфігурація завантажена")
    else:
        print("❌ Помилка завантаження конфігурації")
