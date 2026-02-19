

raw_curl = """
curl 'https://itch.io/g/alienmelon/flower/add-to-collection?source=home&lightbox=true' \
  -H 'accept: application/json, text/javascript, */*; q=0.01' \
  -H 'accept-language: en-US,en;q=0.9,uk;q=0.8,es;q=0.7' \
  -b 'itchio_token=WyJpYkFaIiwxNzcxMjI4MjkyLCJKNms5YVlkWVJMSVY0eDkiXQ%3d%3d%2ebRK2lcYCBc6XqsuTx6mM112fClE%3d; ref%3aregister%3areferrer=https%3a%2f%2fwww%2egoogle%2ecom%2f; ref%3Aregister%3Apage_params=index; ref%3Aregister%3Aaction=header; itchio_refs=[[%22game%22%2C4281560%2C%22index:%22]%2C[%22game%22%2C4246344%2C%22browse:classification:game%22]%2C[%22game%22%2C2863100%2C%22index:%22]%2C[%22game%22%2C4201446%2C%22index:%22]%2C[%22game%22%2C4002987%2C%22index:%22]%2C[%22game%22%2C4270123%2C%22index:%22]%2C[%22game%22%2C709899%2C%22embed:https://jestur.itch.io/ripples%22]%2C[%22game%22%2C3466099%2C%22embed:https://jestur.itch.io/ripples%22]%2C[%22game%22%2C2116405%2C%22embed:https://jestur.itch.io/ripples%22]%2C[%22game%22%2C823489%2C%22browse:classification:game%2Csort:rating%2Ctag:adult%22]%2C[%22game%22%2C911946%2C%22recs:1112425%22]%2C[%22game%22%2C1112425%2C%22recs:2275098%22]%2C[%22game%22%2C2275098%2C%22recs:535841%22]%2C[%22game%22%2C2035584%2C%22browse:classification:physical_game%22]%2C[%22game%22%2C4040561%2C%22browse:classification:game%22]%2C[%22game%22%2C4172670%2C%22index:%22]]; cf_clearance=_ULbNLTVkV7CzNKssBDpyzOwPSa9UQ6K.pSh6wUKk88-1771511700-1.2.1.1-jx8jvgEbK_Yd2FSa7W.meMzbPMWcAAfgIX9xYWkty_n9_W3HCwvbT0aEI59csMMFdv9vrT3DQeetiDnmqQeewzQWolUt4S69fKBnD_ORLloheA7EqqvBHF1FqVZNzDMqot7_ven540A.iQ7ovFqQ9K4JW9ca8FXfdRJWrupMXA_fomxt7GUmP3UwcHvUgVzP0L.8X4NI7hkK1nXbfzh4pJgfckv3YQlaTPWSxlhCciE; itchio=eyJmbGFzaCI6ZmFsc2UsInVzZXIiOnsia2V5IjoiJDJiJDA3JFBcL01Dd2NiRGJuemdOV0tIeGZYYlQuIiwiaWQiOjE2NDUzMDk1LCJzaWQiOjU2MTk5NzA3fX0%3d%0a%2d%2dTtsxJqi1A83EJ5h24jyVxt4%2bgX4%3d' \
  -H 'priority: u=1, i' \
  -H 'referer: https://itch.io/' \
  -H 'sec-ch-ua: "Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"' \
  -H 'sec-ch-ua-arch: "arm"' \
  -H 'sec-ch-ua-bitness: "64"' \
  -H 'sec-ch-ua-full-version: "145.0.7632.76"' \
  -H 'sec-ch-ua-full-version-list: "Not:A-Brand";v="99.0.0.0", "Google Chrome";v="145.0.7632.76", "Chromium";v="145.0.7632.76"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-model: ""' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-ch-ua-platform-version: "15.6.0"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36' \
  -H 'x-requested-with: XMLHttpRequest'
"""

csrf_token = "WyJpYkFaIiwxNzcxMjI4MjkyLCJKNms5YVlkWVJMSVY0eDkiXQ==.bRK2lcYCBc6XqsuTx6mM112fClE="


# ============================================================================
# СКРИПТ ДЛЯ ГЕНЕРАЦІЇ config.json
# ============================================================================

import json
import re


def parse_curl_to_config(curl_command, csrf_token):
    """
    Парсить curl команду та створює config.json для itch.io.
    
    Args:
        curl_command: сирий curl command з браузера
        csrf_token: CSRF токен з форми
        
    Returns:
        dict з конфігурацією
    """
    config = {
        "itchio": {
            "cookies": {},
            "csrf_token": csrf_token,
            "headers": {}
        }
    }
    
    # Парсинг cookies з -b параметра
    cookie_match = re.search(r"-b\s+'([^']+)'", curl_command)
    if cookie_match:
        cookie_string = cookie_match.group(1)
        # Розбиваємо на окремі cookies
        cookies = cookie_string.split('; ')
        for cookie in cookies:
            if '=' in cookie:
                key, value = cookie.split('=', 1)
                config["itchio"]["cookies"][key] = value
    
    # Парсинг headers з -H параметрів
    header_pattern = r"-H\s+'([^:]+):\s*([^']+)'"
    headers = re.findall(header_pattern, curl_command)
    
    # Фільтруємо потрібні headers (пропускаємо sec-ch-ua-* крім основних)
    important_headers = [
        'accept', 'accept-language', 'content-type', 'priority',
        'sec-ch-ua', 'sec-ch-ua-mobile', 'sec-ch-ua-platform',
        'sec-fetch-dest', 'sec-fetch-mode', 'sec-fetch-site',
        'user-agent', 'x-requested-with'
    ]
    
    for header_name, header_value in headers:
        header_name_lower = header_name.lower()
        if header_name_lower in important_headers:
            config["itchio"]["headers"][header_name_lower] = header_value
    
    # Додаємо content-type якщо його немає
    if 'content-type' not in config["itchio"]["headers"]:
        config["itchio"]["headers"]["content-type"] = "application/x-www-form-urlencoded; charset=UTF-8"
    
    return config


def save_config(config, filename='config.json'):
    """
    Зберігає конфігурацію в JSON файл.
    
    Args:
        config: dict з конфігурацією
        filename: ім'я файлу для збереження
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    print(f"✅ Конфігурацію збережено в {filename}")
    print(f"📊 Знайдено cookies: {len(config['itchio']['cookies'])}")
    print(f"📊 Знайдено headers: {len(config['itchio']['headers'])}")
    print(f"📊 CSRF токен: {config['itchio']['csrf_token'][:30]}...")


if __name__ == "__main__":
    print("🔧 Генерація config.json з curl команди...")
    print("=" * 60)
    
    # Генеруємо конфігурацію
    config = parse_curl_to_config(raw_curl, csrf_token)
    
    # Зберігаємо в файл
    save_config(config, 'config.json')
    
    print("\n✅ Готово! Тепер можна запускати process_collections.py")