import json

with open("students.json") as file:
    students = json.load(file)

students.sort(key=lambda s: s["age"])
for s in students:
    print(f"{s['name']} {s['surname']} - {s['age']} yosh")
