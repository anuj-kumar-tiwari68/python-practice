import json

# Given dictionary
Student_data = {"name": "David", "age": 13, "marks": 87}

# 1. Convert dictionary into JSON format
json_data = json.dumps(Student_data)
print("JSON format:", json_data)

# 2. Access the value of age from the given data
print("Age:", Student_data["age"])

# 3. Pretty Print JSON data
pretty_json = json.dumps(Student_data, indent=4)
print("Pretty JSON:\n", pretty_json)

# 4. Sort the JSON keys and write them into a file
sorted_json = json.dumps(Student_data, indent=4, sort_keys=True)
print("Sorted JSON:\n", sorted_json)

with open("student.json", "w") as f:
    f.write(sorted_json)
print("Sorted JSON written to student.json file")
