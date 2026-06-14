# List in python

items = ["Pen", "Pencil", "Copy", "Book", "Table"]

print(len(items))
print(f"first item in the list is {items[0]}")
print(f"last item in the list is {items[-1]}")

# Methods in list 

marks = [65,73,78,98,100]

# Lists are mutable

marks[1] = 83
print(marks)

# Slicing

marks2 = marks[1:4]
print(marks2)
print(marks)

# max and min

print(max(marks))
print(min(marks))