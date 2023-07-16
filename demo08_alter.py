import sqlite3

# Create a database and establish a connection
connection = sqlite3.connect('mydatabase.db')

# Add a new column to the "books" table
connection.execute('ALTER TABLE books ADD COLUMN genre TEXT')

# Display the updated table structure
result = connection.execute('PRAGMA table_info(books)')
table_info = result.fetchall()
for column in table_info:
    print(f"Column Name: {column[1]}, Data Type: {column[2]}")

# Close the database connection
connection.close()
