# import requests
# import json
# import pprint

# """https://note.nkmk.me/python-requests-usage/"""
# ### 基礎
# url = 'https://example.com'
# response = requests.get(url)
# # urlを取得
# print(response.url)
# # status_codeを取得: 200~300以外は失敗
# """300 > res.status_code >= 200ではない場合 → a失敗。"""
# print(response.status_code)
# # レスポンスヘッダを取得: 戻り値は大文字・小文字を区別しない辞書に近い型
# print(response.headers)
# print(response.headers['content-type'])
# print(response.headers['XXXXX']) # 存在しない場合は"None"が返ってくる
# # encoding
# print(response.encoding) # utf-8など
# # text: encoding属性でデコードされたレスポンスの内容が戻ってくる
# print(response.text)
# # バイナリデータ: content属性=デコード前のレスポンス内容（バイト列）
# print(response.content)
# print(response.content.decode(response.encoding)) # デコードすると、textと等価

# ### URLパラメータを指定
# url = 'https://www.google.co.jp/search'
# params = {'q': '日本代表', 'tbm': 'nws'}
# r = requests.get(url, params=params)
# print(r.url)

# ### リクエストヘッダに情報を追加
# url = 'https://www.yahoo.co.jp/'
# ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
# headers = {'User-Agent': ua}
# r_ua = requests.get(url, headers=headers)

# ### リダイレクトの回数を取得する
# url = 'https://en.wikipedia.org'
# r = requests.get(url)
# print(len(r.history)) # 1回リダイレクトがされた
# r_not_redirect = requests.get(url, allow_redirects=False)
# print(r_not_redirect.url) # allow_redirects=Falseでリダイレクトを無効にできる

# ### JASONデータを取得・保存
# url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
# params = {'city': 130010}
# r = requests.get(url, params=params)
# print(r.headers['Content-Type'])
# json_data = r.json() # responseオブジェクトにjson()メソッドを使うと辞書に変換して取得
# pprint.pprint(json_data, depth=2, compact=True)
# with open('/Users/tatsuyaohara/Desktop/download.json', mode="w") as f:
#     json.dump(json_data, f, ensure_ascii=False, indent=4)

# ### 画像やZipファイルをダウンロード
# import os
# url_image = 'https://www.python.org/static/community_logos/python-logo.png'
# r_image = requests.get(url_image)
# print(r_image.headers['Content-Type'])
# # image/png
# filename_image = os.path.basename(url_image)
# print(filename_image)
# # python-logo.png
# with open('data/temp/' + filename_image, 'wb') as f:
#     f.write(r_image.content) # content属性で取得する！

# ### zipファイルのダウンロード
# import os
# url_zip = 'http://www.post.japanpost.jp/zipcode/dl/oogaki/zip/13tokyo.zip'
# r_zip = requests.get(url_zip)
# print(r_zip.headers['Content-Type'])
# filename_zip = os.path.basename(url_zip)
# with open('data/temp/' + filename_zip, mode='wb')as f:
#     f.write(r_zip.content)