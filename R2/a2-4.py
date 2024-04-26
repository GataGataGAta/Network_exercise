from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

# イベントデータを辞書で管理
events = {
    1: {"ID": "1", "Name": "東京オリンピック", "Year": "2020", "Place": "東京"},
    2: {"ID": "2", "Name": "ワールドカップ", "Year": "2022", "Place": "カタール"},
    3: {"ID": "3", "Name": "パリオリンピック", "Year": "2024", "Place": "パリ"}
}

@app.route("/", methods=["GET"])
def input_form():
    # 入力フォームページを返す
    return render_template("a2-4in.html", title="フォームの利用")

@app.route("/", methods=["POST"])
def output():
    # POSTリクエストからidを取得し、整数に変換する
    event_id = request.form.get("id")
    if event_id.isdigit():
        event_id = int(event_id)
        event = events.get(event_id)
        if event:
            # イベントが見つかった場合は、出力ページをレンダリング
            return render_template("a2-4out.html", event=event)
    # イベントが見つからない場合はエラーメッセージとともに入力フォームを再表示
    return render_template("a2-4in.html", title="フォームの利用", error="イベントが見つかりませんでした。")

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5001)
