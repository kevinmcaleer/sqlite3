import sqlite3

connection = sqlite3.connect('mydatabase.db')

connection.execute('''
    CREATE TABLE IF NOT EXISTS employees(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name Text,
                age INTEGER,
                department TEXT
                )
                ''')

# insert data into the table
employee_data = [ 
    ("John Doe", 32, "Sales"),
    ("Jane Doe", 25, "Engineering"),
    ("Fred Doe", 45, "Engineering"),
    ("Chris Doe", 23, "Sales"),
    ("Layla Doe", 35, "Marketing"),
    ("Charlie", 25, "HR"),
    ("Samantha", 30, "Engineering"),
    ("Sam", 27, "Sales"),
    ("Sally", 23, "Marketing"),
    ("Mark", 40, "Engineering"),
    ("Raj", 33, "Engineering"),
]

# connection.executemany('INSERT INTO employees(name, age, department) VALUES(?,?,?)', employee_data)

# query data from the table
result = connection.execute('SELECT * FROM employees ORDER BY age DESC')
data = result.fetchall()

# display the data
for row in data:
    print(f'name: {row[1]}')
    print(f'age: {row[2]}')
    print(f'department: {row[3]}')
    print('')

# write the data to the file
connection.commit()

# close the database connection
connection.close()