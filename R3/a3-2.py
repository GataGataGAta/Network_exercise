from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def table():
    schema = ["ID", "名前", "年", "場所"]
    # 表の属性名のリスト
    table = [[1, "東京オリンピック", "2020", "東京"], [2, "ワールドカップ", "2022", "カタール"], [3, "パリオリンピック", "2024", "パリ"]]
    # 表の属性値のリスト
    return render_template("a3-2.html", title="イベント一覧", schema=schema, table=table)


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=8000)
