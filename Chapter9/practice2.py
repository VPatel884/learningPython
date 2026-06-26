# Create class student that takes 3 marks and has a method average()

class Student:
    marks1 = 88
    marks2 = 98
    marks3 = 94

    def average(self):
        sum = self.marks1 + self.marks2 + self.marks3
        return sum / 3
    
student1 = Student()
print(student1.average())