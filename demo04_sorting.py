# Sorting data

import sqlite3

# Create a database and establish a connection
connection = sqlite3.connect('mydatabase.db')

# Create a table
connection.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        department TEXT
    )
''')

# Insert data into the table
employees_data = [
    (1, "Alice", 28, "Sales"),
    (2, "Bob", 32, "Marketing"),
    (3, "Charlie", 25, "HR"),
    (4, "David", 34, "Operations"),
    (5, "Eva", 29, "Finance"),
    (6, "Frank", 31, "IT"),
    (7, "Grace", 27, "Sales"),
    (8, "Henry", 30, "Operations"),
    (9, "Ivy", 26, "Marketing"),
    (10, "Jack", 33, "HR")
]

connection.executemany('INSERT INTO employees (id, name, age, department) VALUES (?, ?, ?, ?)', employees_data)

# Query and sort data from the table
result = connection.execute('SELECT * FROM employees ORDER BY age ASC')
sorted_data = result.fetchall()

# Display the sorted data
print("Sorted Employees:")
for row in sorted_data:
    print(f"ID: {row[0]}")
    print(f"Name: {row[1]}")
    print(f"Age: {row[2]}")
    print(f"Department: {row[3]}")
    print()

# Write the data to the file
connection.commit()

# Close the database connection
connection.close()
