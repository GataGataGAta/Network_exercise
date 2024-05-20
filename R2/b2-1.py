from flask import Flask, request, render_template

app = Flask(__name__)

# 両替レート
rates = {
    'USD': 110.5,
    'EUR': 130.7,
    'GBP': 150.2
}

@app.route('/')
def index():
    return render_template('b2-1in.html')  # テンプレートファイル名を直接指定

@app.route('/convert', methods=['POST'])
def convert():
    # 入力値を取得
    currency = request.form['currency']
    amount = float(request.form['amount'])

    # 日本円での金額を計算
    if currency in rates:
        converted_amount = amount * rates[currency]
        result = f"{amount} {currency} は {converted_amount:.2f} 円です。"
    else:
        result = "無効な通貨です。"

    # 結果をテンプレートに渡す
    return render_template("b2-1out.html", result=result)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
