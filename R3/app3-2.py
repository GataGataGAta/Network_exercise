import datetime

from flask import Flask, render_template

app = Flask(__name__)


schedule = [
    # 授業スケジュールのリスト
    [datetime.time(9, 0, 0), datetime.time(10, 40, 0)],
    # 1限は9時に始まり，10時40分に終わる．
    [datetime.time(11, 10, 0), datetime.time(12, 50, 0)],
    # 2限は11時10分に始まり，12時50分に終わる．
    [datetime.time(13, 30, 0), datetime.time(15, 10, 0)],
    # 3限は13時30分に始まり，15時10分に終わる．
    [datetime.time(15, 20, 0), datetime.time(17, 0, 0)],
    # 4限は15時20分に始まり，17時に終わる．
    [datetime.time(17, 5, 0), datetime.time(18, 45, 0)],
    # 5限は17時5分に始まり，18時45分に終わる．
]


@app.template_filter("time")
def time_filter(time):
   leftTime = datetime.datetime.now()-datetime.time(16, 27, 30)
   return leftTime

app.jinja_env.filters["period"] = time_filter



@app.route("/")
def timetable():
    return render_template("sample3-2.html", title="授業時間", time=datetime.datetime.now().time())


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=8000)
