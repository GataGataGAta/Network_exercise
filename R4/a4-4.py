from flask import Flask, request, redirect, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("a4-4.html")

@app.route("/add_event", methods=["POST"])
def add_event():
    event_date = request.form["date"]
    event_name = request.form["event"]

    # 日付のバリデーション
    try:
        datetime.strptime(event_date, "%Y-%m-%d")
    except ValueError:
        return "無効な日付です。もう一度入力してください。"

    with open("a4-3.txt", "a", encoding="utf-8") as file:
        file.write(f"{event_date},{event_name}\n")

    return redirect("/")

if __name__ == "__main__":
    app.run(host="localhost", port=8000)
