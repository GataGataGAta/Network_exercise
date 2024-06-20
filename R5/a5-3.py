from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('a5-1.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('a5-3.html')

@app.route('/add-event', methods=['POST'])
def add_event():
    name = request.form['name']
    date = request.form['date']
    place = request.form['place']
    
    conn = get_db_connection()
    conn.execute('INSERT INTO events (name, date, place) VALUES (?, ?, ?)',
                 (name, date, place))
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8000)
