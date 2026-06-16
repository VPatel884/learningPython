# Sets in Python

fruits = {"Apple", "Banana", "Mango"}

print(type(fruits))
print(fruits)

empset = set()
print(type(empset))

# Set Methods
fruits.add("Grapes")
print(fruits)
fruits.remove("Banana")
print(fruits)
fruits.pop()
print(fruits)
fruits.clear()
print(fruits)