# Dictionary

student = {
    "name": "Suraj",
    "city": "Puri",
    "age": 21,
    "rollNo": 42,
    # "name": "Shresth" # key this latest value is returned
}

print(type(student))
# print(student["name"])
print(student)
student["city"] = "Sakti" # Updates if key is already present
print(student)
student["favSub"] = "Computer" # Creates a new key
print(student)
student.pop("age") # To remove a key
print(student)

# Dictionary Methods

print(student.keys())
print(student.values())
print(student.items()) #Returns key-value pair as tuples