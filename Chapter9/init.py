class Student:
    school = "ZXY"

    def __init__(self): # self passed object as parameter ie student1 and student2
        print("Whenever a new object is created I am called automatically.")
        print("Self",self) # Prints objs memory location

student1 = Student()
print("Student 1", student1) # prints same as self
student2 = Student()
print("Student 2", student2) # prints same as self

print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

# It is used to initialize attributes

class Students:
    college= "XYZ"

    def __init__(self, name, course):
        self.name = name
        self.course = course

students1 = Students("Vikram", "BSc")
print("Name of student =",students1.name)
print("Course of student =",students1.course)

students2 = Students("Vikash", "MSc")
print("Name of student =",students2.name)
print("Course of student =",students2.course)