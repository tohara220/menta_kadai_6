# APIを活用して情報を取得する課題です。
APIを活用することにより複雑なプログラムを簡単に構築することができます。

- requestsモジュール  
requestsモジュールを使用してAPIをコールします。  
https://note.nkmk.me/python-requests-usage/

- 楽天API  
https://webservice.rakuten.co.jp/documentation

- 参考  
https://qiita.com/DisneyAladdin/items/d136a04b715de59ade57

# 1
VSCODEにREST Clientプラグインをインストールして楽天の商品APIを実行して結果が返ってくることを確認してみましょう。  
REST Clientの使い方:https://qiita.com/toshi0607/items/c4440d3fbfa72eac840c   
商品検索APIの仕様:https://webservice.rakuten.co.jp/documentation/ichiba-item-search

# 2
以下の仕様を参考にして、任意のキーワードでAPIを検索した時の
商品名と価格の一覧を取得してみましょう
https://webservice.rakuten.co.jp/documentation?doc-name=ichiba-item-search

# 3 
以下のAPIを使って、任意の商品の最安値と最高値を取得してみましょう  
https://webservice.rakuten.co.jp/documentation/ichiba-product-search

# 4
以下のAPIを使って、任意のジャンルのランキング一覧を取得し、CSV出力してみましょう
https://webservice.rakuten.co.jp/documentation/ichiba-item-ranking

# 5
pytestをinstallして、単体テストを実施してみましょう<BR>
- インストール<BR>
`pip install pytest`<BR>
- テスト実行<BR>
`python -m pytest <pyファイルのpath>::<テストしたい関数名> -s`  <BR>

参考<BR>
https://webbibouroku.com/Blog/Article/pytest#outline__3_1

# 6 (オプション課題)
取得した情報をスプレッドシートに自動的に保存してみましょう。
まずは、GCPアカウントが必要なので、GCPアカウントを取得し、サービスアカウントキーjsonをダウンロードしてください。
【注意：このjsonは、GCPへの接続情報を記録した重要なファイルなので、Github(Public)等の公開の場にはUPしてはいけません】
その上で、スプレッドシートAPIを有効化してください。  
[参考](https://note.com/npaka/n/nd522e980d995)
 
# 7  (オプション課題)
 以下のサンプルコードを使用して、スプレッドシートと連携できることを確認してください。
その上で、2で作成した商品情報取得APIと連携させて、スプレッドシートに保存できることを確認してください。
[サンプル](https://github.com/marutoraman/yahoo-api-gss-sample)
- main/ans_main.py 呼び出すコードの参考
- common/spread_sheet_manager.py スプレッドシート管理
- secrets/cred_spreadsheet.json を新規作成し課題６で作成したGCPのサービスアカウントキーjsonを格納する必要があります
 
なお、サンプルコードは、以下のような構造のスプレッドシートと連携することを想定しています。  
jan_listシートにjanコードのリストを記載しておくと  
item_listシートに結果が格納されます。  
https://docs.google.com/spreadsheets/d/1mkHMaovwsNiZrLDteRao0Ec-NV_AwMRn6lJv9RIFNsg/edit?usp=sharing
 