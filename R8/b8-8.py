from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

spring_start = datetime(2024, 4, 8)
spring_end = datetime(2024, 7, 19)
fall_start_first = datetime(2024, 9, 20)
fall_end_first = datetime(2024, 12, 23)
fall_start_second = datetime(2025, 1, 6)
fall_end_second = datetime(2025, 1, 9)

def semester(date):
    if spring_start <= date <= spring_end:
        return "春学期中"
    elif fall_start_first <= date <= fall_end_first or fall_start_second <= date <= fall_end_second:
        return "秋学期中"
    else:
        return "授業期間外"

def countdown(date):
    if spring_start <= date <= spring_end:
        end_date = spring_end
    elif fall_start_first <= date <= fall_end_first:
        end_date = fall_end_first
    elif fall_start_second <= date <= fall_end_second:
        end_date = fall_end_second
    else:
        return None
    return (end_date - date).days

@app.route('/')
def index():
    return render_template('b8-8in.html')

@app.route('/result', methods=['POST'])
def result():
    date_str = request.form['date']
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    sem = semester(date_obj)
    days_left = countdown(date_obj)
    if days_left is not None:
        response = f"{date_str}は{sem}です。授業終了日まであと{days_left}日です。"
    else:
        response = f"{date_str}は{sem}です。"
    return render_template('b8-8out.html', response=response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
