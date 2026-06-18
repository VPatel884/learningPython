# print 1 to 10 using while loop

print("Problem 1")
num = 1

while num <= 10:
    print(num)
    num += 1

# print 10 to 11 using while loop

print("Problem 2")
num1 = 10

while num1 >= 1:
    print(num1)
    num1 -= 1

# Print even number between 1-50

print("Problem 3")

num2 = 1
while num2 <= 50:
    if num2 % 2 == 0:
        print(num2)
    num2 += 1

# Sum of first n natural numbers

print("Problem 4")

n = int(input("Enter a natural number:"))
sum = 0

while n >= 1:
    sum += n
    print(sum)
    n -= 1

print(f"Sum of {n} natural numbers is {sum}")

# print * pattern

print("Problem 5")

starNum = 1
star = ""

while starNum <= 4:
    star += "*"
    print(star)
    starNum += 1
