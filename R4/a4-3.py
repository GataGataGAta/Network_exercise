from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def address3a():
    with open("a4-3.txt", encoding="utf-8") as file:
        data = []
        for text in file:
            data.append(text.split(","))
        schema = ["日付", "イベント名"]
    return render_template("a4-3.html", title="イベント一覧", schema=schema, table=data)


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=8000)