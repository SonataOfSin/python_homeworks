a = input("enter first number: ")
b = input("enter second number: ")
c = input("enter third number: ")
if a > b and a > c:
    print(a, "is the largest number")
elif b > a and b > c:
    print(b, "is the largest number")
else:
    print(c, "is the largest number")
    