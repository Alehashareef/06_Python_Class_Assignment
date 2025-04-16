import json

# Sample data (dictionary)
student = {
    "name": "Aleha",
    "course": "Python",
    "marks": [88, 90, 95],
    "pass": True
}

# Writing JSON to file
with open("student_data.json", "w") as file:
    json.dump(student, file, indent=4)
    print("Data written to student_data.json")

# Reading JSON from file
with open("student_data.json", "r") as file:
    data = json.load(file)
    print("\nLoaded Data from File:")
    print(data)
