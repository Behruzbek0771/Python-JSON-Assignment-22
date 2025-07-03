import json
import os

filename = "students.json"

if not os.path.exists(filename):
    with open(filename, "w") as file:
        json.dump([], file)

name = input("ism: ")
surname = input("familya: ")
age = int(input("yosh: "))

with open(filename, "r") as file:
    students = json.load(file)

students.append({"name": name, "surname": surname, "age": age})

with open(filename, "w") as file:
    json.dump(students, file, indent=2)
