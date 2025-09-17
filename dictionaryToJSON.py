# convert the following dictionary into JSON
import json
# Student_data = {"name":"David", "age":13,"marks":87}
# print(type(Student_data)) # <class 'dict'>
# data = json.dumps(Student_data)
# print(data)
# print(type(data)) # <class 'str'>

# Access the value of age from the given data
# Student_data = """{"name":"David", "age":13,"marks":87}"""
# print(type(Student_data)) # <class 'str'>
# data = json.loads(Student_data) # loads convert the string into python object
# print(data["age"])
# print(type(data["age"])) #<class 'int'>

# pretty print folllowing JSON data
# Student_data = {"name":"David", "age":13,"marks":87}
# data = json.dumps(Student_data, indent=4, separators=(',', '= '))
# print(data)

# sort the following JSON keys and write them into file.
# Student_data = {"name":"David", "age":13,"marks":87}
# f = open("demo.json", "w")
# data = json.dumps(Student_data, indent=4, sort_keys=True)
# f.write(data)
# print("the data has been added to the file")

# Access the nested key "marks" from the following nested data
student_data = """{ "student":
                    {"grade":
                      {"name":"David","marks":87}
                     }
                  }"""

data = json.loads(student_data)
print(data["student"]["grade"]["marks"])

