# Implicit conversion
x = 6 # int
y = 5.6 # float
z = x + y # this automatically converts to float
print(type(x))
print(type(y))
print(type(z))

# Explicit conversion

num1 = input("Enter value: ")
print(type(num1))
convertedNum = int(num1)
print(type(convertedNum))