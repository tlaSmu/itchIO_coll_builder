

raw_curl = """
curl 'https://itch.io/g/spratt/woodworm/add-to-collection?source=home&lightbox=true' \
  -H 'accept: application/json, text/javascript, */*; q=0.01' \
  -H 'accept-language: en-US,en;q=0.9,uk;q=0.8,es;q=0.7' \
  -b 'itchio_token=WyJha1pyIiwxNzY2NTcwODIzLCJYZlZIYzBiZFFDVUc4aHgiXQ%3d%3d%2ejwNkOn%2fZtbSjCRk9we6mfCJ3JCo%3d; ref%3aregister%3areferrer=https%3a%2f%2fwww%2ebing%2ecom%2f; ref%3Aregister%3Apage_params=index; ref%3Aregister%3Aaction=header; allow_nsfw_games=%5b1244135%2c606225%5d; itchio_ca=[[%222:6:1:511571%22%2C[%223:2%22]]%2C[%222:1:1:3583836%22%2C[%223:2%22]]%2C%222:25:1:10519%22%2C%222:16:1:652410%22%2C%222:2:1:3207047%22%2C[%222:1:1:4034035%22%2C[%223:2%22]]%2C[%222:1:1:4270123%22%2C[%223:2%22]]%2C[%222:1:1:2863100%22%2C[%223:2%22]]%2C[%222:1:1:4002987%22%2C[%223:2%22]]%2C[%222:1:1:2502994%22%2C[%223:2%22]]%2C[%222:1:1:735761%22%2C[%223:2%22]]%2C[%222:1:1:4049677%22%2C[%223:2%22]]%2C[%222:1:1:4042177%22%2C[%223:2%22]]%2C%222:2:1:3315518%22%2C%222:2:1:4190765%22%2C%222:2:1:1667814%22%2C%222:2:1:2307914%22%2C%222:2:1:434554%22%2C%222:2:1:3759060%22%2C%222:2:1:2831699%22%2C%222:2:1:2171800%22%2C%222:2:1:1111002%22%2C%222:2:1:2586179%22%2C%222:2:1:532823%22%2C%222:2:1:47367%22%2C%222:2:1:1607077%22%2C%222:2:1:55023%22%2C%222:2:1:1103651%22%2C%222:2:1:3213391%22%2C%222:2:1:2091758%22%2C%222:2:1:1711691%22%2C%222:2:1:2119837%22%2C%222:2:1:4095809%22%2C%222:2:1:4230944%22%2C%222:2:1:1755544%22%2C%222:9:1:2488239%22%2C%222:9:1:2257737%22%2C%222:9:1:1999449%22%2C[%222:7:1:2302682%22%2C[%223:2%22]]]; cf_clearance=jVTZXUdvLPHTkfb9r5PX6SHIfgbmUEm0JHqq1ljs1pk-1770910777-1.2.1.1-rS2KmsNhSLs26aPHbTMAzKI62cl7SFlxtRmtOGqO5yKmuZrmJ6UH1wQNttZ_eUniTl04ONF.BfgL2XfH9Pv6e95tqMMie.3II4dQC1GuiyJTCLCEHw258gyPMIv9YgKaMnWnyRMDlN0VPa7BZO.xl9oeQqLaRyzM1YJ8LPxTm9a3ybjg3q8Npp9tvWFUDzv.wT4h8LWFw5VD8GEL4ZSFRzdMfzzAH0_2OPWSRKX6nyc; itchio=eyJ1c2VyIjp7ImlkIjoxNjM3MzI1OCwia2V5IjoiJDJiJDA3JEdFYTdoRjVVQkpDWk0uY29va2NGeC4iLCJzaWQiOjU1OTExNDU2fSwiZmxhc2giOmZhbHNlLCJuZXdfZ2FtZV9pZCI6ZmFsc2V9%0a%2d%2dhSMpi0qA4JK51i5jfLG57ecplKg%3d; itchio_refs=[[%22game%22%2C4106944%2C%22index:%22]%2C[%22game%22%2C3299044%2C%22embed:https://rosesrot.itch.io/killer-chat-overkill-dlc?embed=randomizer%22]%2C[%22game%22%2C3191595%2C%22embed:https://rosesrot.itch.io/killer-chat-overkill-dlc?embed=randomizer%22]%2C[%22game%22%2C4033860%2C%22embed:https://rosesrot.itch.io/killer-chat-overkill-dlc?embed=randomizer%22]%2C[%22game%22%2C2979281%2C%22embed:https://rosesrot.itch.io/killer-chat-overkill-dlc?embed=randomizer%22]%2C[%22game%22%2C3886945%2C%22embed:https://rosesrot.itch.io/killer-chat-overkill-dlc?embed=randomizer%22]%2C[%22game%22%2C531708%2C%22embed:https://runninblood.itch.io/windy-hills-16x16-top-down-asset-pack%22]%2C[%22game%22%2C2211527%2C%22embed:https://runninblood.itch.io/windy-hills-16x16-top-down-asset-pack%22]%2C[%22game%22%2C2306404%2C%22embed:https://runninblood.itch.io/windy-hills-16x16-top-down-asset-pack%22]%2C[%22game%22%2C2302682%2C%22index:my_recs%22]%2C[%22game%22%2C868166%2C%22embed:https://snatsgames.itch.io/twistedworldremake%22]%2C[%22game%22%2C4270123%2C%22browse:classification:game%22]%2C[%22game%22%2C1755544%2C%22browse:classification:game%22]%2C[%22game%22%2C4230944%2C%22browse:classification:game%22]%2C[%22game%22%2C4095809%2C%22browse:classification:game%22]%2C[%22game%22%2C2119837%2C%22browse:classification:game%22]%2C[%22game%22%2C1711691%2C%22browse:classification:game%22]%2C[%22game%22%2C2091758%2C%22browse:classification:game%22]%2C[%22game%22%2C3213391%2C%22browse:classification:game%22]%2C[%22game%22%2C2684103%2C%22embed:https://robobarbie.itch.io/blooming-panic%22]]' \
  -H 'priority: u=1, i' \
  -H 'referer: https://itch.io/' \
  -H 'sec-ch-ua: "Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"' \
  -H 'sec-ch-ua-arch: "arm"' \
  -H 'sec-ch-ua-bitness: "64"' \
  -H 'sec-ch-ua-full-version: "144.0.7559.110"' \
  -H 'sec-ch-ua-full-version-list: "Not(A:Brand";v="8.0.0.0", "Chromium";v="144.0.7559.110", "Google Chrome";v="144.0.7559.110"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-model: ""' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-ch-ua-platform-version: "15.7.3"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36' \
  -H 'x-requested-with: XMLHttpRequest'
"""

csrf_token = "WyJha1pyIiwxNzY2NTcwODIzLCJYZlZIYzBiZFFDVUc4aHgiXQ==.jwNkOn/ZtbSjCRk9we6mfCJ3JCo="


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