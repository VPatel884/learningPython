# print number 1 to 10 except multiple of 2

for num in range(11):
    if (num % 2 == 0):
        continue
    else:
        print(num)

# Enter 5 countries from user and print one by one

countries = []

for num in range(5):
    country = input("Enter country name: ")
    countries.append(country)

print("Countries Entered Are:")

for country in countries:
    print(country)