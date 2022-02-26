import requests
import urllib
import pprint
import pandas as pd
from history.api import * 

# 定数
APPLICATION_ID = 1085338819672671222
RAKUTEN_ITEM_SEARCH_URL = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
RAKUTEN_PRODUCT_SEARCH_URL = "https://app.rakuten.co.jp/services/api/Product/Search/20170426"
RAKUTEN_RANKING_SEARCH_URL = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628"

def test_item_search(url):
    res = item_search(url = RAKUTEN_ITEM_SEARCH_URL)
    # 成り立つ条件を書く。
    # assert len(res["Items"]) >= 1
    # # 何か帰って来ればOKとする
    # assert res["Items"][0]["Item"]["itemCode"]
    