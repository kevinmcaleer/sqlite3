import sqlite3

# Create a database and establish a connection
connection = sqlite3.connect('mydatabase.db')

# Create a table
connection.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        year INTEGER
    )
''')

# Insert data into the table
books_data = [
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925),
    ("To Kill a Mockingbird", "Harper Lee", 1960),
    ("Pride and Prejudice", "Jane Austen", 1813)
]

connection.executemany('INSERT INTO books (title, author, year) VALUES (?, ?, ?)', books_data)

# Query data from the table
result = connection.execute('SELECT * FROM books')
data = result.fetchall()

# Display the retrieved data
for row in data:
    print(f"Title: {row[1]}")
    print(f"Author: {row[2]}")
    print(f"Year: {row[3]}")
    print()

# Close the database connection
connection.close()