import requests
import json

def trim_data(payload):
    removed_faulty = []
    for x in payload:
        if x['price'] != None:
            removed_faulty.append(x)
    for x in removed_faulty:
        if 'release_date' in x:
            del x['release_date']
        if 'release_type' in x:
            del x['release_type']
        if 'item_state' in x:
            del x['item_state']
        if 'genres' in x:
            del x['genres']
        if 'pubs' in x:
            del x['pubs']
        if 'devs' in x:
            del x['devs']
        if 'overview' in x:
            del x['overview']
        if 'image' in x:
            del x['image']
        if 'documentation' in x:
            del x['documentation']
        if 'game_specific' in x:
            del x['game_specific']
        if 'alt_titles' in x:
            del x['alt_titles']
        if 'mc' in x:
            del x['mc']
        if 'links' in x:
            del x['links']
        if 'exe_time' in x:
            del x['exe_time']
        if 'error' in x:
            del x['error']
        if 'parent_id' in x:
            del x['parent_id']
        if 'updated_at' in x:
            del x['updated_at']
        if 'metascore' in x:
            del x['metascore']
        if 'has_vgpc' in x:
            del x['has_vgpc']
        
    return removed_faulty

def normalize_prices(payload):
    for x in payload:
        x['price']['Loose'] = x['price']['Loose'] // 100
        x['price']['CIB'] = x['price']['CIB'] // 100
        x['price']['ManualPrice'] = x['price']['ManualPrice'] // 100
        x['price']['BoxPrice'] = x['price']['BoxPrice'] // 100
    return payload

def add_margin(payload):
    for x in payload:
        con_amount = x['price']['Loose'] + x['price']['ManualPrice'] + x['price']['BoxPrice']
        if x['price']['CIB'] == 0:
            x['price']['Margin'] = -1
            x['price']['MarginInDollars'] = 0
        else:
            margin =  float(con_amount) / float(x['price']['CIB'])
            x['price']['ConstructedAmount'] = con_amount
            x['price']['MarginInDollars'] = x['price']['CIB'] - con_amount
            x['price']['Margin'] = 1 - margin
    return payload

def number_of_pages():
    url = "https://www.gameye.app/api/deep_search?offset=0&limit=100&title=++&platforms=6&order=0&asc=1&country=1"
    payload = ""
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    total_count = response.json()['full_count']
    return total_count // 100 + 1

def get_full_game_list(pages):
    total_records = []
    pages = pages - 1
    for page in range(0, pages):
        url = f"https://www.gameye.app/api/deep_search?offset={page}00&limit=100&title=++&platforms=6&order=0&asc=1&country=1"
        payload = ""
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        records = json.loads(response.text)['records']
        for record in records:
            total_records.append(record)
    return total_records

def transform_data_for_d_frame(total_records):
    game_list = []
    for record in total_records:        
        if record['price']['Margin'] > 0:
            game_data ={
                "title": record['title'],
                "Gameye_id": record['id'],
                "Category_id": record['category_id'],
                "Platform_id": record['platform_id'],
                "Country_id": record['country_id'],
                "CIB": record['price']['CIB'],
                "Constructed_price": str(record['price']['Loose']+record['price']['ManualPrice']+record['price']['BoxPrice']),
                "CartPrice": record['price']['Loose'],
                "ManualPrice": record['price']['ManualPrice'],
                "BoxPrice": record['price']['BoxPrice'],
                "Margin": record['price']['Margin'],
                "MarginInDollars": record['price']['MarginInDollars']
            }
            game_list.append(game_data)
    return game_list