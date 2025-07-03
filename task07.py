import json

with open("students.json") as file:
    students = json.load(file)

total = sum(s["age"] for s in students)
avg = total / len(students)
print(f"{avg:.1f}")
