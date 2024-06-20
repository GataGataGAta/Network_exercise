from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

@app.route("/", methods=["GET", "POST"])
def calculator():
    if 'x' not in session:
        session['x'] = 0 

    x = session['x']
    y = None
    error = None

    if request.method == "POST":
        try:
            y = int(request.form.get("y"))
            operation = request.form.get("operation")

            if operation == "add":
                x += y
            elif operation == "subtract":
                x -= y
            elif operation == "multiply":
                x *= y
            elif operation == "divide":
                if y == 0:
                    error = "0で割ることはできません。"
                else:
                    x //= y  

            session['x'] = x 

        except ValueError:
            error = "有効な整数を入力してください。"

    return render_template("a4-2.html", x=x, error=error)

if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=8000)
