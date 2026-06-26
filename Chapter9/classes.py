# Object Oriented Programming in Python

# Class Creation

class MyVehicle:
    model = "Audi V8"
    color = "Black" #attribute
    fuelType = "Diesel"
    mileage = 17

    def myFirstCar(self): # Function inside class is called methods
        print("My First Car is", self.model)

# Object Creation

car = MyVehicle()
car.myFirstCar()
