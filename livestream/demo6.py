import sqlite3

connection = sqlite3.connect('mydatabase.db')

# Delete a specific book by its ID from the "books" table
# book_id_to_delete = 4


connection.execute('ALTER TABLE employees ADD COLUMN transport TEXT')

connection.commit()

# result = connection.execute('SELECT * FROM books')

# print("books")
# for row in result.fetchall():
#     print(f'Title: {row[1]}, Author: {row[2]}, Year: {row[3]}')