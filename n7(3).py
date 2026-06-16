import random
original_list = []
for i in range(20):
    random_num = random.randint(-50, 50)
    original_list.append(random_num)
even_list = []
for num in original_list:
    if num % 2 == 0:
        even_list.append(num)
print("strating list: ")
print(original_list)
print("\neven numbers list: ")
print(even_list)