# Create a class and 2 objects with different attributes

class Laptop:
    brand = "Sony"
    RAM = "16GB"
    price = "1 Lakh"

laptop1 = Laptop()
laptop1.brand = "Acer"
laptop1.RAM = "8GB"
laptop1.price = "50 Thousand"
print(laptop1.brand)

laptop2 = Laptop()
print(laptop2.brand)