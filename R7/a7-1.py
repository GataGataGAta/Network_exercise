from flask import Flask, request, render_template, redirect
import sqlite3
import re
from datetime import datetime

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('events.db')
    conn.row_factory = sqlite3.Row
    return conn

# Display events
@app.route('/')
def index():
    conn = get_db_connection()
    events = conn.execute('SELECT * FROM events').fetchall()
    conn.close()
    today = datetime.today().strftime('%Y-%m-%d')
    return render_template('a7-1.html', events=events, today=today)

# Add event
@app.route('/add-event', methods=['POST'])
def add_event():
    name = request.form['name']
    date = request.form['date']
    place = request.form['place']
    conn = get_db_connection()
    conn.execute('INSERT INTO events (name, date, place) VALUES (?, ?, ?)', (name, date, place))
    conn.commit()
    conn.close()
    return redirect('/')

# Delete event
@app.route('/delete-event', methods=['POST'])
def delete_event():
    event_id = request.form['id']
    conn = get_db_connection()
    conn.execute('DELETE FROM events WHERE id = ?', (event_id,))
    conn.commit()
    conn.close()
    return redirect('/')

# Search event
@app.route('/search-event', methods=['GET'])
def search_event():
    search_name = request.args.get('search-name')
    search_date = request.args.get('search-date')
    search_place = request.args.get('search-place')

    query = 'SELECT * FROM events WHERE 1=1'
    params = []
    
    if search_name:
        query += ' AND name REGEXP ?'
        params.append(search_name)
    
    if search_date:
        query += ' AND date = ?'
        params.append(search_date)
    
    if search_place:
        query += ' AND place LIKE ?'
        params.append(f'%{search_place}%')

    conn = get_db_connection()
    conn.create_function("REGEXP", 2, lambda expr, item: re.search(expr, item) is not None)
    events = conn.execute(query, params).fetchall()
    conn.close()
    today = datetime.today().strftime('%Y-%m-%d')
    return render_template('a7-1.html', events=events, today=today)

if __name__ == '__main__':
    app.run(debug=True)
