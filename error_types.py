
a = input("enter first number: ")
b = input("enter second number: ")
c = float(a)
d = float(b)
try:
    print(c/d)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Program execution completed.")











 