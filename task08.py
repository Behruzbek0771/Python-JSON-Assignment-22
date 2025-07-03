import json

with open("students.json") as file:
    students = json.load(file)

top = max(students, key=lambda s: s["age"])
print(f"{top['name']} {top['surname']} - {top['age']} yosh")
