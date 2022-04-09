import requests
import pandas as pd
import time
import random

def get_name(list):
    if list is None:
        return None
    filtered_list = [i["name"] for i in list]
    return ', '.join(map(str, filtered_list))

def check_and_insert_winery(t):
    if "name" in t["vintage"]["wine"]["winery"]:
        return t["vintage"]["wine"]["winery"]["name"]
    else:
        return None

def check_and_insert_origin(t):
    if "name" in t["vintage"]["wine"]["region"]:
        return t["vintage"]["wine"]["region"]["name"]
    else:
        return None

def check_and_insert_country(t):
    if "name" in t["vintage"]["wine"]["region"]["country"]:
        return t["vintage"]["wine"]["region"]["country"]["name"]
    else:
        return None

def check_and_insert_wine(t):
    if "name" in t["vintage"]["wine"] and "year" in t["vintage"]:
        return f'{t["vintage"]["wine"]["name"]} {t["vintage"]["year"]}' #(+ its year)
    else:
        return None

def check_and_insert_variety(t):
    if "varietal_name" in t["vintage"]["wine"]["style"]:
        return t["vintage"]["wine"]["style"]["varietal_name"]
    else:
        return None

def check_and_insert_grape(t):
    if "grapes" in t["vintage"]["wine"]["style"]:
        return get_name(t["vintage"]["wine"]["style"]["grapes"])
    else:
        return None

def check_and_insert_price(t):
    return t["price"]["amount"] if "amount" in t["price"] else None #euros

def check_and_insert_rating(t):
    if "ratings_average" in t["vintage"]["statistics"]:
        return t["vintage"]["statistics"]["ratings_average"] #0-10
    else:
        return None

def check_and_insert_body(t):
    if "body" in t["vintage"]["wine"]["style"]:
        return t["vintage"]["wine"]["style"]["body"] #0-10
    else:
        return None

def check_and_insert_acidity(t):
    if "acidity" in t["vintage"]["wine"]["style"]:
        return t["vintage"]["wine"]["style"]["acidity"] #(0-10)
    else:
        return None

def check_and_insert_description(t):
    if "description" in t["vintage"]["wine"]["style"]:
        return t["vintage"]["wine"]["style"]["description"]
    else:
        return None

def check_and_insert_food(t):
    if "food" in t["vintage"]["wine"]["style"]:
        return get_name(t["vintage"]["wine"]["style"]["food"])
    else:
        return None

def check_and_insert_id(t):
    return t["vintage"]["id"] if "id" in t["vintage"] else None

def get_data(page):
    r = requests.get(
        "https://www.vivino.com/api/explore/explore",
        params = {
            "country_code": "ES",
            "country_codes[]":"es",
            "currency_code":"EUR",
            "grape_filter":"varietal",
            "min_rating":"1",
            "order_by":"", #price
            "order":"", #asc
            "page": page,
            "price_range_max":"500",
            "price_range_min":"0",
            "wine_type_ids[]":"1",
            "language": "es"
        },
        headers= {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"
        }
    )

    return [
        (
            check_and_insert_wine(t),
            check_and_insert_winery(t),
            check_and_insert_origin(t),
            check_and_insert_country(t),
            check_and_insert_variety(t),
            check_and_insert_grape(t),
            check_and_insert_price(t),
            check_and_insert_rating(t),
            check_and_insert_body(t),
            check_and_insert_acidity(t),
            check_and_insert_description(t),
            check_and_insert_food(t),
            time.strftime("%Y-%m-%d"),
            "vivino",
        )
        for t in r.json()["explore_vintage"]["matches"]
    ]

results=[]
for page in range(1, 81): #81 pages in total
    results += get_data(page)
    # time.sleep(random.randint(1,5))
    print('Page', page, 'scraped!')

dataframe = pd.DataFrame(results, columns=['wine','winery', 'origin', 'country', 'variety', 'grape', 'price', 'rating', 'body', 'acidity', 'description', 'food', 'date', 'source'])
print(dataframe)
dataframe.to_csv('wines_vivino.csv', index=False, encoding='utf-8')
