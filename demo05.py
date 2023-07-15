import sqlite3

# Create a database and establish a connection
connection = sqlite3.connect('mydatabase.db')

# Create the "Students" table
connection.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')

# Create the "Courses" table
connection.execute('''
    CREATE TABLE IF NOT EXISTS Courses (
        id INTEGER PRIMARY KEY,
        name TEXT,
        student_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES Students(id)
    )
''')

# Insert data into the "Students" table
students_data = [
    (1, 'Alice', 18),
    (2, 'Bob', 19),
    (3, 'Charlie', 20)
]

connection.executemany('INSERT INTO Students (id, name, age) VALUES (?, ?, ?)', students_data)

# Insert data into the "Courses" table
courses_data = [
    (1, 'Math', 1),
    (2, 'Science', 2),
    (3, 'History', 3)
]

connection.executemany('INSERT INTO Courses (id, name, student_id) VALUES (?, ?, ?)', courses_data)

# Query and display data from the "Students" and "Courses" tables
result = connection.execute('''
    SELECT Students.name, Courses.name
    FROM Students
    INNER JOIN Courses ON Students.id = Courses.student_id
''')

# Write the data to the file
connection.commit()

print("Student - Course Relationship:")
for row in result.fetchall():
    print(f"Student: {row[0]}, Course: {row[1]}")

# Close the database connection
connection.close()
