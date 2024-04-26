from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

with open("a1-3.html", mode="r", encoding="utf-8") as file:
    template = file.read()


routes = []
# ルートを保存するグローバル変数を初期化する


def route(path, method):
    routes.append((path, method))
    # ルートのパスとそれに応じた処理（メソッド）をタプルとしてroutesに登録する．


route("/id1", "id1")
route("/id2", "id2")
route("/id3", "id3")
# 2つのルートと処理を登録する．


class MyServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        _url = urlparse(self.path)
        # クラス内変数_urlにアクセスパスを代入する．
        for r in routes:
            # routesの要素を順にrに代入する．
            if r[0] == _url.path:
                eval("self." + r[1] + "()")
                # パスに応じたメソッドを実行する．
                break
                # 登録しているパスであった場合は処理を実行し，for文を抜ける．
        else:
            self.error()
            # routesに登録されていない場合は，errorメソッドを実行する．

    def id1(self):
        self.send_response(200)
        self.end_headers()
        html = template.format(ID="1", Name="東京オリンピック", Year="2020", Place="東京")
        self.wfile.write(html.encode("utf-8"))
        return

    def id2(self):
        self.send_response(200)
        self.end_headers()
        html = template.format(ID="2", Name="ワールドカップ", Year="2022", Place="カタール")
        self.wfile.write(html.encode("utf-8"))
        return

    def id3(self):
        self.send_response(200)
        self.end_headers()
        html = template.format(ID="3", Name='<font color = "blue">パリオリンピック</font>', Year="2024", Place="フランス")
        self.wfile.write(html.encode("utf-8"))
        return
    
    def error(self):
        self.send_error(404, "CANNOT ACCESS!!")
        # エラーコード(404)とメッセージを表示する．
        return


HTTPServer(("", 8000), MyServerHandler).serve_forever()