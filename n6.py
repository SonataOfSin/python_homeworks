
number = int(input("enter number: "))
factorial = 1
if number < 0:
    print("factorial of an negative number does not exist.")
elif number == 0:
    print("factorial of 0 is 1.")
else:
    for i in range(1, number + 1): # number + 1 anu am ricxvis chatvlit
        factorial *= i  
    print(f"factorial of {number} is {factorial}")