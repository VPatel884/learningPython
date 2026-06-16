# List of programming languages is given
# Convert it into set and print number of unique languages

programmingList = ["Python", "Java", "C++", "Python", "Java", "C"]

# converting list to set

programmingSet = set(programmingList) # Similar to type casting
print(type(programmingSet))
print(programmingSet)
print("Number of programming languages is", len(programmingSet))