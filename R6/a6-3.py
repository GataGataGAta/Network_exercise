from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # ダミーデータの作成
    data = {
        'ID': [1, 2, 3],
        '名称': ['東京オリンピック', 'ワールドカップ', 'パリオリンピック'],
        '時期': ['2020年', '2022年', '<font color="green">2024年</font>'],
        '場所': ['東京', 'カタール', 'パリ']
    }

    # DataFrameの作成
    df = pd.DataFrame(data)

    # HTMLページをレンダリングして返す
    return render_template('a6-3.html', rows=df.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
