firstName = 'Vikash'
middleName = "Kumar"
lastName = '''Patel'''

# String Concatination
fullName = firstName + " " + middleName + " " + lastName
print(fullName)

# String length
print(len(fullName)) #Datatype is int

# String indexing
print(firstName[0]) #V
print(firstName[5]) #h

# Slicing
print(fullName[0:6])
print(fullName[7:12])
print(fullName[13:18])

# Formatted String
print(f"{firstName} {lastName}")
