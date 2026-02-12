import requests

headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9,uk;q=0.8,es;q=0.7',
    'priority': 'i',
    'referer': 'purple-sugar.itch.io/witchs-bound',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-storage-access': 'active',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
}

response = requests.get('https://img.itch.zone/aW1nLzk2NTM2MjIucG5n/50x50%23/lHkdk6.png', headers=headers)


cookies = {
    'itchio_token': 'WyJha1pyIiwxNzY2NTcwODIzLCJYZlZIYzBiZFFDVUc4aHgiXQ%3d%3d%2ejwNkOn%2fZtbSjCRk9we6mfCJ3JCo%3d',
    'ref%3aregister%3areferrer': 'https%3a%2f%2fwww%2ebing%2ecom%2f',
    'ref%3Aregister%3Apage_params': 'index',
    'ref%3Aregister%3Aaction': 'header',
    'allow_nsfw_games': '%5b1244135%2c606225%5d',
    'cf_clearance': 'a3RaupCa0X9BVaGMRtOtTvu1jZjT7XamngpPqkfsY_4-1770896359-1.2.1.1-.C1PZj627QJhn2VQwMGXfx2P_lEntSh_3R1nVHfW5bVIccLFJYyJIZBEDbdC28XThBL4MW80EcNVUej13eoc5luiR936inJW0bQivTVP7UN.d6ntEsmWvtNXPBFIPcO0MbXX7_nNqE5Px4vKNWESYwuVxdSN2pDNkoRG.2u5PPurrLEJCfqJT2VmI1wHNUBFsuD4HG0Jx8_u8P.uXWH5CdQqIZgaq.4N9w8DOQRMfpc',
    'itchio': 'eyJ1c2VyIjp7InNpZCI6NTU5MDQ5MTIsImlkIjoxNjM3MTQxOCwia2V5IjoiJDJiJDA3JG53b1hsUGhCQlBqUldFZmVxZWdRSXUifSwiZmxhc2giOmZhbHNlLCJuZXdfZ2FtZV9pZCI6ZmFsc2V9%0a%2d%2drnIeHBz60NpNqulxP%2bGYNB4ljoY%3d',
    'itchio_refs': '[[%22game%22%2C4270123%2C%22index:%22]%2C[%22game%22%2C4034035%2C%22index:%22]%2C[%22game%22%2C3207047%2C%22browse:classification:game%22]%2C[%22game%22%2C652410%2C%22search:final%20fantasy%207%20r%22]%2C[%22game%22%2C674537%2C%22search:final%20fantasy%207%20r%22]%2C[%22game%22%2C1019869%2C%22search:sonic%20fan%22]%2C[%22game%22%2C369416%2C%22search:Harry%20Potter%22]%2C[%22game%22%2C1699890%2C%22search:Freedom%20Planet%202%22]%2C[%22game%22%2C3430806%2C%22search:Tekken%207%22]%2C[%22game%22%2C693458%2C%22search:Gacha%20Club%22]%2C[%22game%22%2C1297665%2C%22search:Huggy%20Wuggy%22]%2C[%22game%22%2C961532%2C%22search:sonic%20mania%22]%2C[%22game%22%2C3245288%2C%22search:Free%20Beat%20Maker%22]%2C[%22game%22%2C76706%2C%22search:Sands%20Of%20Salzaar%20Free%22]%2C[%22game%22%2C1115956%2C%22search:Gacha%20Cute%22]%2C[%22game%22%2C3874513%2C%22search:Mavis%20Beacon%22]%2C[%22game%22%2C436400%2C%22search:Dead%20Island%22]%2C[%22game%22%2C1819272%2C%22search:Grand%20Theft%20Auto%203%22]%2C[%22game%22%2C324096%2C%22search:Pizza%20Tower%22]%2C[%22game%22%2C349310%2C%22search:Visio%20Desktop%20App%20Download%22]]',
    'itchio_ca': '[[%222:6:1:511571%22%2C[%223:2%22]]%2C[%222:1:1:3583836%22%2C[%223:2%22]]%2C%222:25:1:10519%22%2C%222:16:1:652410%22%2C%222:2:1:3207047%22%2C[%222:1:1:4034035%22%2C[%223:2%22]]%2C[%222:1:1:4270123%22%2C[%223:2%22]]]',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,uk;q=0.8,es;q=0.7',
    'priority': 'u=1, i',
    'referer': 'purple-sugar.itch.io/witchs-bound',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'itchio_token=WyJha1pyIiwxNzY2NTcwODIzLCJYZlZIYzBiZFFDVUc4aHgiXQ%3d%3d%2ejwNkOn%2fZtbSjCRk9we6mfCJ3JCo%3d; ref%3aregister%3areferrer=https%3a%2f%2fwww%2ebing%2ecom%2f; ref%3Aregister%3Apage_params=index; ref%3Aregister%3Aaction=header; allow_nsfw_games=%5b1244135%2c606225%5d; cf_clearance=a3RaupCa0X9BVaGMRtOtTvu1jZjT7XamngpPqkfsY_4-1770896359-1.2.1.1-.C1PZj627QJhn2VQwMGXfx2P_lEntSh_3R1nVHfW5bVIccLFJYyJIZBEDbdC28XThBL4MW80EcNVUej13eoc5luiR936inJW0bQivTVP7UN.d6ntEsmWvtNXPBFIPcO0MbXX7_nNqE5Px4vKNWESYwuVxdSN2pDNkoRG.2u5PPurrLEJCfqJT2VmI1wHNUBFsuD4HG0Jx8_u8P.uXWH5CdQqIZgaq.4N9w8DOQRMfpc; itchio=eyJ1c2VyIjp7InNpZCI6NTU5MDQ5MTIsImlkIjoxNjM3MTQxOCwia2V5IjoiJDJiJDA3JG53b1hsUGhCQlBqUldFZmVxZWdRSXUifSwiZmxhc2giOmZhbHNlLCJuZXdfZ2FtZV9pZCI6ZmFsc2V9%0a%2d%2drnIeHBz60NpNqulxP%2bGYNB4ljoY%3d; itchio_refs=[[%22game%22%2C4270123%2C%22index:%22]%2C[%22game%22%2C4034035%2C%22index:%22]%2C[%22game%22%2C3207047%2C%22browse:classification:game%22]%2C[%22game%22%2C652410%2C%22search:final%20fantasy%207%20r%22]%2C[%22game%22%2C674537%2C%22search:final%20fantasy%207%20r%22]%2C[%22game%22%2C1019869%2C%22search:sonic%20fan%22]%2C[%22game%22%2C369416%2C%22search:Harry%20Potter%22]%2C[%22game%22%2C1699890%2C%22search:Freedom%20Planet%202%22]%2C[%22game%22%2C3430806%2C%22search:Tekken%207%22]%2C[%22game%22%2C693458%2C%22search:Gacha%20Club%22]%2C[%22game%22%2C1297665%2C%22search:Huggy%20Wuggy%22]%2C[%22game%22%2C961532%2C%22search:sonic%20mania%22]%2C[%22game%22%2C3245288%2C%22search:Free%20Beat%20Maker%22]%2C[%22game%22%2C76706%2C%22search:Sands%20Of%20Salzaar%20Free%22]%2C[%22game%22%2C1115956%2C%22search:Gacha%20Cute%22]%2C[%22game%22%2C3874513%2C%22search:Mavis%20Beacon%22]%2C[%22game%22%2C436400%2C%22search:Dead%20Island%22]%2C[%22game%22%2C1819272%2C%22search:Grand%20Theft%20Auto%203%22]%2C[%22game%22%2C324096%2C%22search:Pizza%20Tower%22]%2C[%22game%22%2C349310%2C%22search:Visio%20Desktop%20App%20Download%22]]; itchio_ca=[[%222:6:1:511571%22%2C[%223:2%22]]%2C[%222:1:1:3583836%22%2C[%223:2%22]]%2C%222:25:1:10519%22%2C%222:16:1:652410%22%2C%222:2:1:3207047%22%2C[%222:1:1:4034035%22%2C[%223:2%22]]%2C[%222:1:1:4270123%22%2C[%223:2%22]]]',
}

params = {
    'source': 'game',
    'lightbox': 'true',
}

response = requests.get(
    'https://purple-sugar.itch.io/witchs-bound/add-to-collection',
    params=params,
    cookies=cookies,
    headers=headers,
)


headers = {
    'sec-ch-ua-platform': '"macOS"',
    'Referer': 'https://purple-sugar.itch.io/witchs-bound',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
    'sec-ch-ua-mobile': '?0',
}

response = requests.get('https://static.itch.io/selectize.min.css?1770761333', headers=headers)


headers = {
    'sec-ch-ua-platform': '"macOS"',
    'Referer': 'https://purple-sugar.itch.io/witchs-bound',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
    'sec-ch-ua-mobile': '?0',
}

response = requests.get('https://static.itch.io/selectize.min.js?1770761333', headers=headers)


headers = {
    'Origin': 'https://papercookies.itch.io',
    'sec-ch-ua-platform': '"macOS"',
    'Referer': 'https://static.itch.io/game.css?1770761333',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
    'sec-ch-ua-mobile': '?0',
}

response = requests.get('https://static.itch.io/fonts/lato-v14-latin-900.woff2', headers=headers)


headers = {
    'sec-ch-ua-platform': '"macOS"',
    'Referer': 'https://static.itch.io/game.css?1770761333',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
    'sec-ch-ua-mobile': '?0',
}

response = requests.get('https://static.itch.io/images/loader.gif', headers=headers)


cookies = {
    'itchio_token': 'WyJha1pyIiwxNzY2NTcwODIzLCJYZlZIYzBiZFFDVUc4aHgiXQ%3d%3d%2ejwNkOn%2fZtbSjCRk9we6mfCJ3JCo%3d',
    'ref%3aregister%3areferrer': 'https%3a%2f%2fwww%2ebing%2ecom%2f',
    'ref%3Aregister%3Apage_params': 'index',
    'ref%3Aregister%3Aaction': 'header',
    'allow_nsfw_games': '%5b1244135%2c606225%5d',
    'cf_clearance': 'a3RaupCa0X9BVaGMRtOtTvu1jZjT7XamngpPqkfsY_4-1770896359-1.2.1.1-.C1PZj627QJhn2VQwMGXfx2P_lEntSh_3R1nVHfW5bVIccLFJYyJIZBEDbdC28XThBL4MW80EcNVUej13eoc5luiR936inJW0bQivTVP7UN.d6ntEsmWvtNXPBFIPcO0MbXX7_nNqE5Px4vKNWESYwuVxdSN2pDNkoRG.2u5PPurrLEJCfqJT2VmI1wHNUBFsuD4HG0Jx8_u8P.uXWH5CdQqIZgaq.4N9w8DOQRMfpc',
    'itchio': 'eyJ1c2VyIjp7InNpZCI6NTU5MDQ5MTIsImlkIjoxNjM3MTQxOCwia2V5IjoiJDJiJDA3JG53b1hsUGhCQlBqUldFZmVxZWdRSXUifSwiZmxhc2giOmZhbHNlLCJuZXdfZ2FtZV9pZCI6ZmFsc2V9%0a%2d%2drnIeHBz60NpNqulxP%2bGYNB4ljoY%3d',
    'itchio_refs': '[[%22game%22%2C4270123%2C%22index:%22]%2C[%22game%22%2C4034035%2C%22index:%22]%2C[%22game%22%2C3207047%2C%22browse:classification:game%22]%2C[%22game%22%2C652410%2C%22search:final%20fantasy%207%20r%22]%2C[%22game%22%2C674537%2C%22search:final%20fantasy%207%20r%22]%2C[%22game%22%2C1019869%2C%22search:sonic%20fan%22]%2C[%22game%22%2C369416%2C%22search:Harry%20Potter%22]%2C[%22game%22%2C1699890%2C%22search:Freedom%20Planet%202%22]%2C[%22game%22%2C3430806%2C%22search:Tekken%207%22]%2C[%22game%22%2C693458%2C%22search:Gacha%20Club%22]%2C[%22game%22%2C1297665%2C%22search:Huggy%20Wuggy%22]%2C[%22game%22%2C961532%2C%22search:sonic%20mania%22]%2C[%22game%22%2C3245288%2C%22search:Free%20Beat%20Maker%22]%2C[%22game%22%2C76706%2C%22search:Sands%20Of%20Salzaar%20Free%22]%2C[%22game%22%2C1115956%2C%22search:Gacha%20Cute%22]%2C[%22game%22%2C3874513%2C%22search:Mavis%20Beacon%22]%2C[%22game%22%2C436400%2C%22search:Dead%20Island%22]%2C[%22game%22%2C1819272%2C%22search:Grand%20Theft%20Auto%203%22]%2C[%22game%22%2C324096%2C%22search:Pizza%20Tower%22]%2C[%22game%22%2C349310%2C%22search:Visio%20Desktop%20App%20Download%22]]',
    'itchio_ca': '[[%222:6:1:511571%22%2C[%223:2%22]]%2C[%222:1:1:3583836%22%2C[%223:2%22]]%2C%222:25:1:10519%22%2C%222:16:1:652410%22%2C%222:2:1:3207047%22%2C[%222:1:1:4034035%22%2C[%223:2%22]]%2C[%222:1:1:4270123%22%2C[%223:2%22]]]',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,uk;q=0.8,es;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://papercookies.itch.io',
    'priority': 'u=1, i',
    'referer': 'https://purple-sugar.itch.io/witchs-bound',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'itchio_token=WyJha1pyIiwxNzY2NTcwODIzLCJYZlZIYzBiZFFDVUc4aHgiXQ%3d%3d%2ejwNkOn%2fZtbSjCRk9we6mfCJ3JCo%3d; ref%3aregister%3areferrer=https%3a%2f%2fwww%2ebing%2ecom%2f; ref%3Aregister%3Apage_params=index; ref%3Aregister%3Aaction=header; allow_nsfw_games=%5b1244135%2c606225%5d; cf_clearance=a3RaupCa0X9BVaGMRtOtTvu1jZjT7XamngpPqkfsY_4-1770896359-1.2.1.1-.C1PZj627QJhn2VQwMGXfx2P_lEntSh_3R1nVHfW5bVIccLFJYyJIZBEDbdC28XThBL4MW80EcNVUej13eoc5luiR936inJW0bQivTVP7UN.d6ntEsmWvtNXPBFIPcO0MbXX7_nNqE5Px4vKNWESYwuVxdSN2pDNkoRG.2u5PPurrLEJCfqJT2VmI1wHNUBFsuD4HG0Jx8_u8P.uXWH5CdQqIZgaq.4N9w8DOQRMfpc; itchio=eyJ1c2VyIjp7InNpZCI6NTU5MDQ5MTIsImlkIjoxNjM3MTQxOCwia2V5IjoiJDJiJDA3JG53b1hsUGhCQlBqUldFZmVxZWdRSXUifSwiZmxhc2giOmZhbHNlLCJuZXdfZ2FtZV9pZCI6ZmFsc2V9%0a%2d%2drnIeHBz60NpNqulxP%2bGYNB4ljoY%3d; itchio_refs=[[%22game%22%2C4270123%2C%22index:%22]%2C[%22game%22%2C4034035%2C%22index:%22]%2C[%22game%22%2C3207047%2C%22browse:classification:game%22]%2C[%22game%22%2C652410%2C%22search:final%20fantasy%207%20r%22]%2C[%22game%22%2C674537%2C%22search:final%20fantasy%207%20r%22]%2C[%22game%22%2C1019869%2C%22search:sonic%20fan%22]%2C[%22game%22%2C369416%2C%22search:Harry%20Potter%22]%2C[%22game%22%2C1699890%2C%22search:Freedom%20Planet%202%22]%2C[%22game%22%2C3430806%2C%22search:Tekken%207%22]%2C[%22game%22%2C693458%2C%22search:Gacha%20Club%22]%2C[%22game%22%2C1297665%2C%22search:Huggy%20Wuggy%22]%2C[%22game%22%2C961532%2C%22search:sonic%20mania%22]%2C[%22game%22%2C3245288%2C%22search:Free%20Beat%20Maker%22]%2C[%22game%22%2C76706%2C%22search:Sands%20Of%20Salzaar%20Free%22]%2C[%22game%22%2C1115956%2C%22search:Gacha%20Cute%22]%2C[%22game%22%2C3874513%2C%22search:Mavis%20Beacon%22]%2C[%22game%22%2C436400%2C%22search:Dead%20Island%22]%2C[%22game%22%2C1819272%2C%22search:Grand%20Theft%20Auto%203%22]%2C[%22game%22%2C324096%2C%22search:Pizza%20Tower%22]%2C[%22game%22%2C349310%2C%22search:Visio%20Desktop%20App%20Download%22]]; itchio_ca=[[%222:6:1:511571%22%2C[%223:2%22]]%2C[%222:1:1:3583836%22%2C[%223:2%22]]%2C%222:25:1:10519%22%2C%222:16:1:652410%22%2C%222:2:1:3207047%22%2C[%222:1:1:4034035%22%2C[%223:2%22]]%2C[%222:1:1:4270123%22%2C[%223:2%22]]]',
}

data = {
    'source': 'game',
    'csrf_token': 'WyJha1pyIiwxNzY2NTcwODIzLCJYZlZIYzBiZFFDVUc4aHgiXQ==.jwNkOn/ZtbSjCRk9we6mfCJ3JCo=',
    'collection[id]': '6974230',
    'add_to': 'new',
    'collection[title]': 'My Favourites 56',
    'collection[blurb]': 'My Favourites Blurb text',
}

response = requests.post('https://purple-sugar.itch.io/witchs-bound/add-to-collection', cookies=cookies, headers=headers, data=data)

print(response.text)
