from api import *
from run_api import run_api
import pprint

APPLICATION_ID = 1085338819672671222

def test_run_api():
    """APIのresponseをjsonで返す関数"""
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
    res = run_api(url=url, params={"keyword": "PS5", "applicationId": APPLICATION_ID, "format": "json"})
    
    assert len(res["Items"]) >= 1
    assert res["Items"][0]["Item"]["itemCode"]
    
def test_kadai_1():
    keyword = "PS5"
    res = kadai_1(keyword=keyword)
    
    assert len(res["Items"]) >= 1
    assert res["Items"][0]["Item"]["itemCode"]

def test_kadai_2():
    keyword = "PS5"
    res = kadai_2(keyword=keyword)
    
    assert len(res["Items"]) >= 1
    assert res["Items"][0]["Item"]["itemName"]
    assert res["Items"][0]["Item"]["itemPrice"]

def test_kadai_3():
    keyword = "PS5"
    res = kadai_3(keyword=keyword)
    
    assert len(res["Products"]) >= 1
    assert res["Products"][0]["Product"]["productName"]
    assert res["Products"][0]["Product"]["maxPrice"]
    assert res["Products"][0]["Product"]["minPrice"]

def test_kadai_4():
    # 100371: レディースファッション
    genreid = "100371"
    res = kadai_4(genreid=genreid)
    
    assert len(res["Items"]) >= 1
    assert res["Items"][0]["Item"]["itemName"]
    assert res["Items"][0]["Item"]["rank"]