# Tuples in python

# Tuples are like list but they are immutable

studentsTuple = ("Vikash", "Vikram", "Vishal", "Vikash")

# Empty Tuple
EmTuple = ()
singleTup = (28) # Tuple with single value is treated as int
print(type(studentsTuple))
print(type(EmTuple))
print(type(singleTup))

# Tuple Mwthods
print(studentsTuple.index("Vikram"))
print(studentsTuple.count("Vikash"))