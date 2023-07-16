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

# Write the data to the file
connection.commit()

# Close the database connection
connection.close()