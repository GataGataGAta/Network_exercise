import sqlite3
from flask import Flask, g, render_template

app = Flask(__name__)

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect("a5-1.db")
        g.db.row_factory = sqlite3.Row  # 追加: 結果を辞書形式で取得する
    return g.db

def close_db():
    db = g.pop("db", None)
    if db is not None:
        db.close()

@app.route("/", methods=["GET"])
def database():
    db = get_db()
    db.execute("CREATE TABLE IF NOT EXISTS events (name TEXT, date TEXT, place TEXT)")  # テーブル作成の追加
    cur = db.execute("SELECT * FROM events")  
    table = cur.fetchall()
    close_db()
    schema = ["ID", "名前", "日時", "場所"]  # 適宜修正すること
    return render_template("a5-2.html", title="DBテスト", schema=schema, table=table)

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)
