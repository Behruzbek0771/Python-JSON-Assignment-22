import json
import csv

with open("students.json") as jsonfile:
    students = json.load(jsonfile)

with open("students.csv", "w", newline="") as csvfile:
    fieldnames = ["name", "surname", "age"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for student in students:
        writer.writerow(student)
