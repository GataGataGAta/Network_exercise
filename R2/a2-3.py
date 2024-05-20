from flask import Flask, render_template

app = Flask(__name__)

name = ["東京オリンピック", "ワールドカップ", "パリオリンピック"]
id = ["1", "2", "3"]
year = ["2020","2022","2024"]
place = ["東京","カタール",'<font color = "blue">パリ</font>']

@app.route("/id<num>")
def page(num):
    try:
        Name = "{}".format(name[int(num) - 1])
        Year = "{}".format(year[int(num) - 1])
        Place = "{}".format(place[int(num) - 1])
    except Exception:
        message = "ページは見つかりませんでした"
    return render_template("a2-3.html", title="表示テスト", Name=Name, ID = id[int(num) - 1], Year=Year, Place=Place)


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=5001)