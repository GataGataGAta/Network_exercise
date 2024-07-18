from flask import Flask, request, render_template, redirect
import sqlite3
import re
from datetime import datetime

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    return conn

# Display books
@app.route('/')
def index():
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM books').fetchall()
    conn.close()
    return render_template('b7-1.html', books=books)

# Add book
@app.route('/add-book', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    published_date = request.form['published_date']
    conn = get_db_connection()
    conn.execute('INSERT INTO books (title, author, published_date) VALUES (?, ?, ?)', (title, author, published_date))
    conn.commit()
    conn.close()
    return redirect('/')

# Delete book
@app.route('/delete-book', methods=['POST'])
def delete_book():
    book_id = request.form['id']
    conn = get_db_connection()
    conn.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()
    conn.close()
    return redirect('/')

# Search book
@app.route('/search-book', methods=['GET'])
def search_book():
    search_title = request.args.get('search-title')
    search_author = request.args.get('search-author')
    search_published_date = request.args.get('search-published_date')

    query = 'SELECT * FROM books WHERE 1=1'
    params = []
    
    if search_title:
        query += ' AND title REGEXP ?'
        params.append(search_title)
    
    if search_author:
        query += ' AND author REGEXP ?'
        params.append(search_author)
    
    if search_published_date:
        query += ' AND published_date = ?'
        params.append(search_published_date)

    conn = get_db_connection()
    conn.create_function("REGEXP", 2, lambda expr, item: re.search(expr, item) is not None)
    books = conn.execute(query, params).fetchall()
    conn.close()
    return render_template('b7-1.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
