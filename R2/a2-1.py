import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def template():
    dt = datetime.datetime.now()
    return render_template("a2-1.html")


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=5001)