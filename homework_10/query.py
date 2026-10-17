import threading
import math

# 1. ძირითადი ფუნქცია მარტივობის შესამოწმებლად
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# 2. ფუნქცია, რომელსაც თითოეული ნაკადი შეასრულებს
def check_prime_worker(n, results):
    if is_prime(n):
        results[n] = f"{n} არის მარტივი"
    else:
        results[n] = f"{n} შედგენილია (არ არის მარტივი)"

# მოცემული სია
num_list = [17, 25, 74, 199, 101, 41, 39, 50, 20, 19, 51]

# შედეგების შესანახი ლექსიკონი და ნაკადების სია
results = {}
threads = []

if __name__ == "__main__":

    for num in num_list:
        t = threading.Thread(target=check_prime_worker, args=(num, results))
        threads.append(t)
        t.start()


    for t in threads:
        t.join()

    for num in num_list:
        print(results[num])