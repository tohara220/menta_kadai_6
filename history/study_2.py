import csv
import sys
import codecs
import math
import random
import requests
from time import sleep
import re

args = sys.argv
shopName = args[1]


url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
payload = {
    'applicationId': 1085338819672671222,
    'hits': 30,#一度のリクエストで返してもらう最大個数（MAX30)
    'shopCode': shopName,#ショップID
    'page':1,#何ページ目か
    'postageFlag':1,#送料込みの商品に限定
    }
r = requests.get(url, params=payload)
resp = r.json()
total = int(resp['count'])
Max = total/30 + 1
print("【num of item】",total)
print("【num of page】",Max)
print("===================================")

counter = 0
for i in resp['Items']:
    counter = counter + 1
    item = i['Item']
    name = item['itemName']
    print('【No.】'+ str(counter))
    print('【Name】' + str(name[:30].encode('utf-8')) + '...')
    print('【Price】' + '¥' +str(item['itemPrice']))
    print('【URL】',item['itemUrl'])
    print('【shop】',item['shopName'])
    print('【text】', item['itemCaption'])