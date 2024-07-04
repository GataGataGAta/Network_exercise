from flask import Flask, make_response, render_template, request

app = Flask(__name__)

events = {
    1: {"ID": "1", "Name": "東京オリンピック", "Year": "2020", "Place": "東京"},
    2: {"ID": "2", "Name": "ワールドカップ", "Year": "2022", "Place": "カタール"},
    3: {"ID": "3", "Name": "パリオリンピック", "Year": "2024", "Place": "パリ"}
}

@app.route("/", methods=["GET", "POST"])
def input_form():
    event_id = request.cookies.get("last_event_id")
    event = None
    error = None
    
    if request.method == "POST":
        event_id = request.form.get("id")
        event_id = int(event_id)
        event = events.get(event_id)
        if event:
            response = make_response(render_template("a6-4out.html", event=event))
            response.set_cookie("last_event_id", str(event_id), max_age=60 * 60 * 24 * 120)  # クッキーに保存
            return response
        else:
            error = "イベントが見つかりませんでした。"
             
    if event_id and event_id.isdigit():
        event_id = int(event_id)
        event = events.get(event_id)
    
    return render_template("a6-4in.html", title="フォームの利用", event=event, error=error)

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
