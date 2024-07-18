from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

events = [
    {"id": 1, "name": "東京オリンピック", "date": "2020-08-01"},
    {"id": 2, "name": "カタールワールドカップ", "date": "2022-09-15"},
    {"id": 3, "name": "パリオリンピック", "date": "2024-07-30"},
    {"id": 4, "name": "アメリカワールドカップ", "date": "2026-02-01"},
    {"id": 5, "name": "ロスオリンピック", "date": "2028-07-20"},
]

@app.route('/')
def index():
    today = datetime.now().date()
    events_with_future_flag = [
        {
            "id": event["id"],
            "name": event["name"],
            "date": event["date"],
            "is_future": datetime.strptime(event["date"], "%Y-%m-%d").date() > today
        }
    for event in events]
    return render_template('b8-7.html', events=events_with_future_flag)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
