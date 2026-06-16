#შექმენით მთელი რიცხვების მინიმუმ 5 ელემენტიანი სია, გამოთვალეთ ყველა რიცხვის ჯამი და საშუალო, არ გამოიყენოთ ჩაშენებული ფუნქციე
int_list = [1, 2, 3, 5, 8]
sum = 0
count = 0
for num in int_list:
    sum += num
    count += 1
average = sum / count
print(f"list of numbers: {int_list}")
print(f"sum is: {sum}")
print(f"average is: {average}")

