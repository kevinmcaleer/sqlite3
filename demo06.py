import sqlite3

# Create a database and establish a connection
connection = sqlite3.connect('mydatabase.db')

# Delete a specific book by its ID from the "books" table
book_id_to_delete = 6
connection.execute('DELETE FROM books WHERE id = ?', (book_id_to_delete,))

# Write the data to the file
connection.commit()

result = connection.execute('SELECT * FROM books')

print("Books")
for row in result.fetchall():
    print(f"Student: {row[0]}, Course: {row[1]}")

# Close the database connection
connection.close()
