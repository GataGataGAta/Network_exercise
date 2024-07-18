from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)
events = [
    {"id": 1, "name": "東京オリンピック", "date": "2020-08-01"},
    {"id": 2, "name": "カタールワールドカップ", "date": "2022-09-15"},
    {"id": 3, "name": "パリオリンピック", "date": "2024-07-30"},
]

@app.route('/')
def index():
    return render_template('b8-3in.html', events=events)

@app.route('/output')
def output():
    event_id = int(request.args.get('event', 0))
    event = next((event for event in events if event["id"] == event_id), None)
    if event:
        return render_template('b8-3out.html', event=event)
    else:
        return "<h1>Event not found</h1>", 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)
