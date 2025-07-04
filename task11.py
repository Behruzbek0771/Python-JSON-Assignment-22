import os
import json

if not os.path.exists("students1.json"):
    with open("students1.json", "w") as file:
        json.dump([], file)
