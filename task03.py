import json

with open("students.json", "r") as file:
    students = json.load(file)

new_student = {"name": "Shahzoda", "surname": "Nazarova", "age": 22}
students.append(new_student)

with open("students.json", "w") as file:
    json.dump(students, file, indent=2)
