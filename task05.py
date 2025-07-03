import json

with open("students.json") as file:
    students = json.load(file)

for student in students:
    if student["age"] > 20:
        print(f"{student['name']} {student['surname']} - {student['age']} yosh")
 