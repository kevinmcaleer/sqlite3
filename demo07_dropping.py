import sqlite3

# Create a database and establish a connection
connection = sqlite3.connect('mydatabase.db')

# Delete a specific book by its ID from the "books" table
book_id_to_delete = 1
# connection.execute('DROP TABLE books')

# Write the data to the file
connection.commit()

# Query the "sqlite_master" table to retrieve table names
result = connection.execute("SELECT name FROM sqlite_master WHERE type='table';")

print("Tables")
for row in result.fetchall():
    print(f"table: {row[0]}")

# Close the database connection
connection.close()
