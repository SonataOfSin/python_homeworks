amount_left = 50
valid_bills = [5, 10, 20]
print(f"you need to pay{amount_left}lari")
while amount_left > 0: 
    inserted_bill = int(input("enter bill: "))
    if inserted_bill not in valid_bills:
        print("invalid bill")
    else:
        amount_left -= inserted_bill
        if amount_left > 0:
            print("f(paid:{inserted_bill}lari, left to pay:{amount_left}lari)")
print("done")
if amount_left < 0:
    change = abs(amount_left) # abs ფუნქცია - აშორებს რადგან ხურდა არ იყოს -10 ლარი, არამედ 10.
    print(f"your change is {change}lari")
elif amount_left == 0:
    print("no change}")