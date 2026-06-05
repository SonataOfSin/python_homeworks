x = int(input("enter amount of second: "))
y = x//3600
remaining_seconds = x%3600
z = remaining_seconds//60
w = remaining_seconds%60
print(y, "hour", z, "minute", w, "second")