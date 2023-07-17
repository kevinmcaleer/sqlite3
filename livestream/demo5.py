import sqlite3

connection = sqlite3.connect('mydatabase.db')

connection.execute('''
    CREATE TABLE IF NOT EXISTS Students(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name Text,
                     age INTEGER
                   )
                   ''')

connection.execute('''
    CREATE TABLE IF NOT EXISTS Courses(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name Text,
                   student_id INTEGER,
                   FOREIGN KEY(student_id) REFERENCES Students(id)
                   )
                   ''')

students_data = [
    ("John Doe", 18),
    ("bob", 19),
    ("Charlie", 20),
]

courses_data = [
    ("Math", 1),
    ("Science", 2),
    ("History", 3)
]

connection.executemany('INSERT INTO Students(name, age) VALUES(?,?)', students_data)
connection.executemany('INSERT INTO Courses(name, student_id) VALUES(?,?)', courses_data)

results = connection.execute('''
SELECT Students.name, Courses.name
FROM Students
INNER JOIN Courses ON Students.id = Courses.student_id
''')
                             
connection.commit()

print("Student - Course Relationship")
for row in results.fetchall():
    print(f'Student: {row[0]}, Course: {row[1]}')

connection.close()