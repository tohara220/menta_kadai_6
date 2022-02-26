import requests
import urllib
import pprint
import pandas as pd

# 定数
APPLICATION_ID = 1085338819672671222
RAKUTEN_ITEM_SEARCH_URL = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
RAKUTEN_PRODUCT_SEARCH_URL = "https://app.rakuten.co.jp/services/api/Product/Search/20170426"
RAKUTEN_RANKING_SEARCH_URL = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628"


def item_search(url):
    """課題2: 任意のキーワードでAPIを検索した時の商品名と価格の一覧を取得してみましょう"""
    result = requests.get(url)
    result_json = result.json()
    for json_obj in result_json["Items"]:
        item_name = json_obj["Item"]["itemName"]
        item_price = json_obj['Item']['itemPrice']
        print(item_name, item_price)
        return result_json
    
def product_search(url):
    """課題3: 任意の商品の最安値と最高値を取得してみましょう"""
    result = requests.get(url)
    result_json = result.json()
    for json_obj in result_json["Products"]:
        print(json_obj["Product"]["productName"], json_obj["Product"]["maxPrice"], json_obj["Product"]["minPrice"])
        
def ranking_search(url):
    """課題4: 任意のジャンルのランキング一覧を取得し、CSV出力してみましょう"""
    result = requests.get(url)
    result_json = result.json()
    df = pd.DataFrame(columns=["順位", "商品名"])
    for json_obj in result_json["Items"]:
        item_name = json_obj["Item"]["itemName"]
        rank = json_obj["Item"]["rank"]
        
        df = df.append({
            "商品名": item_name,
            "順位": rank
        }, ignore_index=True)
    df.to_csv("output_rakuten_ranking.csv", encoding="utf-8_sig")

def main():
    # ### 課題2
    # keyword = "鬼滅"
    # url = f"{RAKUTEN_ITEM_SEARCH_URL}?format=json&keyword={keyword}&applicationId={APPLICATION_ID}"
    # item_search(url)
    
    # ### 課題3
    # keyword = "鬼滅"
    # url = f"{RAKUTEN_PRODUCT_SEARCH_URL}?format=json&keyword={keyword}&applicationId={APPLICATION_ID}"
    # product_search(url)
    
    ### 課題4
    genre_id = 100283
    url = f"{RAKUTEN_RANKING_SEARCH_URL}?applicationId={APPLICATION_ID}"
    ranking_search(url)
main()