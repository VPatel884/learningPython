# Program to enter three names and add them in a list. Print it's length and the list.

name1 = input("Enter first name: ")
name2 = input("Enter second name: ")
name3 = input("Enter third name: ")

nameList = []
nameList.append(name1)
nameList.append(name2)
nameList.append(name3)

print(nameList)
print(len(nameList))