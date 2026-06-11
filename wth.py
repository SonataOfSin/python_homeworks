try:
    age = int(input("enter age: "))
    if age < 0:
        raise ValueError("negative age is not allowed")

except ValueError:
    print("enter numbers")

else:
    if age < 18:
        print("child")
    else:
        print("adult")

finally:
    print("done")










 