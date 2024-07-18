from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('b8-6.html')

@app.route('/countdown', methods=['POST'])
def countdown():
    event_name = request.form['name']
    event_date = request.form['date']
    try:
        event_date_obj = datetime.strptime(event_date, "%Y-%m-%d")
        today = datetime.now()
        days_left = (event_date_obj - today).days
        response = f"{event_name}まで、あと{days_left}日です。"
    except ValueError:
        response = "Invalid date format. Please use YYYY-MM-DD."

    return render_template('b8-6.html', response=response)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
