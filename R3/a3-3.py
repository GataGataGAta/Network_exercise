from flask import Flask, render_template
import datetime

app = Flask(__name__)

schema = ["ID", "名前", "年", "場所", "時間"]
table = [
    [1, "東京オリンピック", "2020", "東京", datetime.datetime(2020, 7, 23)],
    [2, "ワールドカップ", "2022", "カタール", datetime.datetime(2022, 11, 20)],
    [3, "パリオリンピック", "2024", "パリ", datetime.datetime(2024, 7, 26)]
]

@app.template_filter('days_left')
def days_left(event_date):
    now = datetime.datetime.now()
    left = event_date - now
    return left.days  

@app.route("/")
def timetable():
    return render_template('a3-3.html', title="イベント一覧", schema=schema, table=table, time=datetime.datetime.now().time())

if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")
