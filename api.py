import requests
import urllib
from pprint import pprint
import os
import pandas as pd
import datetime

from run_api import run_api

# 変数
now = datetime.datetime.now()
ymdhms = f"{now:%Y%m%d%H%M%S}"

# 定数
CSV_PATH = "output_csv"
APPLICATION_ID = 1085338819672671222
ITEM_SEARCH_URL = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
ITEM_PRICE_SEARCH_URL = "https://app.rakuten.co.jp/services/api/Product/Search/20170426"
RANKING_URL = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628"

def kadai_1(keyword):
    """課題1. 楽天の商品APIを実行して結果が返ってくることを確認してみましょう。"""
    params = {
        "format": "json",
        "keyword": keyword,
        "applicationId": APPLICATION_ID,
        "minPrice": 1000
    }
    res_json = run_api(ITEM_SEARCH_URL, params=params)
    print(res_json)
    return res_json

def kadai_2(keyword):
    """任意のキーワードでAPIを検索した時の 商品名と価格の一覧を取得してみましょう。"""
    params = {
        "applicationId": APPLICATION_ID,
        "format": "json",
        "keyword": keyword        
    }
    df = pd.DataFrame()
    res_json = run_api(ITEM_SEARCH_URL, params=params)
    for res in res_json["Items"]:
        item_name = res["Item"]["itemName"]
        item_price = res["Item"]["itemPrice"]
        df = df.append({
            "商品名": item_name,
            "価格": item_price
        },ignore_index=True)
    df.to_csv(f"{CSV_PATH}/NAME|PRICE_{ymdhms}_{keyword}.csv")
    return res_json

def kadai_3(keyword):
    """任意の商品の最安値と最高値を取得してみましょう"""
    params = {
        "applicationId": APPLICATION_ID,
        "keyword": keyword,
    }
    res_json = run_api(ITEM_PRICE_SEARCH_URL, params)
    
    df = pd.DataFrame()
    
    for res in res_json["Products"]:
        item_name = res["Product"]["productName"]
        max_price = res["Product"]["maxPrice"]
        min_price = res["Product"]["minPrice"]
        df = df.append({
            "商品名": item_name,
            "最高価格": max_price,
            "最低価格": min_price
        },ignore_index=True)
    df.to_csv(f"{CSV_PATH}/MAX|MIN_PRICE_{ymdhms}_{keyword}.csv")
    return res_json
  
def kadai_4(genreid):
    """任意のジャンルのランキング一覧を取得し、CSV出力してみましょう"""
    params = {
        "applicationId": APPLICATION_ID,  
        "genreId" : genreid
    }
    res_json = run_api(RANKING_URL, params)
    
    df = pd.DataFrame()
    for res in res_json["Items"]:
        item_name = res["Item"]["itemName"]
        item_rank = res["Item"]["rank"]
        
        df = df.append({
            "商品名": item_name,
            "最高価格": item_rank
        },ignore_index=True)
    df.to_csv(f"{CSV_PATH}/RANK_{ymdhms}_{genreid}.csv")
    return res_json

# 実行
if __name__ == "__main__":
    # CSVファイル保存先ディレクトリの作成
    os.makedirs(CSV_PATH, exist_ok=True)
    # キーワードの入力
    keyword = input("検索キーワードを入力してください。>>")
    
    ### 課題実行ファイル
    # 課題1
    
    kadai_1(keyword)
    kadai_2(keyword)
    kadai_3(keyword)
    genreid = input("ジャンルIDを入力してください。>>")
    kadai_4(genreid)