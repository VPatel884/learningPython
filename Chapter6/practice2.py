# print 1 to 10 and write "Vikash" on multiple of 5

for item in range(1, 11, 1):
    if (item % 5 == 0):
        print("Vikash")
    else:
        print(item)

# Print square of each number from 1 to 10

for num in range(1, 11, 1):
    print(num ** 2)

# Print table for entered number i.e. 6 * 1 = 6 to 6 * 10 = 60

value = int(input("Enter a number:"))

for num in range (1, 11, 1):
    print(f"{value} * {num} = {value * num}")

# Print "Vikash" five times in upper case

for value in range(1, 6, 1):
    print("Vikash".upper())

# Print each value from given tuple 

countries = ("Malaysia", "Vietnam", "Italy", "Bhutan")

for country in countries:
    print(country)