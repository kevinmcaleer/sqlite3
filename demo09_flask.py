from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Set up SQLite database connection
DATABASE = 'mydatabase.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    # Retrieve data from the database
    conn = get_db_connection()
    cursor = conn.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()

    # Render the template with the data
    return render_template('index.html', books=books)

@app.route('/add_book', methods=['POST'])
def add_book():
    # Retrieve form data
    title = request.form['title']
    author = request.form['author']
    year = request.form['year']

    # Insert data into the database
    conn = get_db_connection()
    conn.execute('INSERT INTO books (title, author, year) VALUES (?, ?, ?)', (title, author, year))
    conn.commit()
    conn.close()

    # Redirect back to the main page
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
