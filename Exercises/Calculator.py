num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
oper = input("Operation to be performed(+, -, *, /, % {Remender}, // {Floor Devision}):")

if (oper == "+"):
    print(f"{num1} + {num2} = {num1 + num2}")
elif (oper == "-"):
    print(f"{num1} - {num2} = {num1 - num2}")
elif (oper == "*"):
    print(f"{num1} * {num2} = {num1 * num2}")
elif (oper == "/"):
    print(f"{num1} / {num2} = {num1 / num2}")
elif (oper == "%"):
    print(f"{num1} % {num2} = {num1 % num2}")
elif (oper == "//"):
    print(f"{num1} // {num2} = {num1 // num2}")
else:
    print("Invalid Operation. Try Again!")   

