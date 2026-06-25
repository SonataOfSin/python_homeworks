
#function 1

def sum_user_numbers(times=5):
    total_sum = 0
    for i in range(times):
        while True:
            try:
                number = float(input(f"please enter number({i+1}/{times}): "))
                total_sum += number
                break
            except ValueError:
                print("error. please enter valid number.")
    return total_sum

#function 2

def split_odd_even(*args):
    odds = []
    evens = []
    for number in args:
        if number % 2 == 0:
            evens.append(number)
        else:
            odds.append(number)
    return odds, evens

#function 3

import string
def count_words(sentence):
    sentence = sentence.lower()
    for char in string.punctuation:
        sentence = sentence.replace(char, "")
    words = sentence.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1            
    return word_counts


#function 3

from functools import reduce

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 15},
    {"name": "Keyboard", "price": 25},
    {"name": "Monitor", "price": 150},
    {"name": "Power", "price": 100},
    {"name": "Pad", "price": 10},
]
cheap_products = list(filter(lambda p: p["price"] < 100, products))
print("price lower than 100:")
print(cheap_products)
print("-" * 40)
product_info = list(map(lambda p: f"{p['name']} - {p['price']}₾", products))
print("names and prices of all products:")
for item in product_info:
    print(item)
print("-" * 40)
sorted_products = sorted(products, key=lambda p: p["price"])
print("sorted products based on price:")
print(sorted_products)
print("-" * 40)
total_price = reduce(lambda acc, p: acc + p["price"], products, 0)
print(f"total price of products: {total_price}")

#function 5

def recursive_sum(n):
    if n <= 1:
        return n
    else:
        return n + recursive_sum(n - 1)

