from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def time_display():
    dt = datetime.now()
    if dt.second % 2 == 0:
        message = '<font color = "red">今は{a}時{b}分{c}秒です</font>'.format(a=dt.hour, b=dt.minute, c=dt.second)
    else:
        message = '<font color = "blue">今は{a}時{b}分{c}秒です</font>'.format(a=dt.hour, b=dt.minute, c=dt.second)
    return render_template('a2-2.html', message=message)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
