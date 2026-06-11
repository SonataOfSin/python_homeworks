a = input("enter a number: ")
b = input("enter a number: ")
x = input("enter an equation: ")
if x == "+":
    print(int(a) + int(b))
if x == "-":
    print(int(a) - int(b))
if x == "*":
    print(int(a) * int(b))
if x == "/":
    print(int(a) / int(b))
    if int(b) == 0:
        print("Error: Division by zero is not allowed.")
if x == "//":
    print(int(a) // int(b))
    if int(b) == 0:
        print("Error: Division by zero is not allowed.")
if x == "%":
    print(int(a) % int(b))
    if int(b) == 0:
        print("Error: Division by zero is not allowed.")
if x == "**":
    print(int(a) ** int(b))
    if int(b) == 0:
        print("Error: Division by zero is not allowed.")
