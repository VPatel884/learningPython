# Take input and print middle 3 and last 2 characters

str = input("Enter the string: ")
mid = len(str)//2
midThree = str[mid-1:mid+2]
lastTwo = str[-2:] # Reverse Indexing
print(midThree)
print(lastTwo)