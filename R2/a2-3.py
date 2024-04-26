from flask import Flask, render_template

app = Flask(__name__)

name = ["東京オリンピック", "ワールドカップ", "パリオリンピック"]
id = ["1", "2", "3"]
year = ["2020","2022","2024"]
place = ["東京","カタール",'<font color = "blue">パリ</font>']

@app.route("/id<num>")
# ルートがidで始まる場合に呼び出される．idより後の部分は変数numに代入される．
def page(num):
    try:
        Name = "{}".format(name[int(num) - 1])
        Year = "{}".format(year[int(num) - 1])
        Place = "{}".format(place[int(num) - 1])
    except Exception:
        # numの値が正しくない場合は例外が生じる．
        message = "ページは見つかりませんでした"
    return render_template("a2-3.html", title="表示テスト", Name=Name, ID = id[int(num) - 1], Year=Year, Place=Place)


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=5001)