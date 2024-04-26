import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def template():
    dt = datetime.datetime.now()
    message = "今日は{a}年{b}月{c}日です．".format(a=dt.year, b=dt.month, c=dt.day)
    return render_template("sample2-2.html", title="表示テスト", message=message)
    # sample2-2.htmlの{{title}}と{{message}}の部分をそれぞれ置換する．


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=5001)