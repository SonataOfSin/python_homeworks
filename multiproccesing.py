from concurrent.futures import ProcessPoolExecutor
# ეს იმპორტი გვეხმარება პროგრამის ასინქრონულად გაშვებაში
import math

def is_prime(n: int) -> tuple[int, bool]:
    """
    ამოწმებს არის თუ არა გადაცემული რიცხვი მარტივი.
    აბრუნებს ტუპლს: (რიცხვი, True/False)
    """
    if n < 2:
        return n, False
    if n == 2:
        return n, True
    if n % 2 == 0:
        return n, False

    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return n, False

    return n, True


if __name__ == "__main__":
    num_list = [17, 25, 74, 199, 101, 41, 39, 50, 20, 19, 51]

    with ProcessPoolExecutor() as executor:
        results = list(executor.map(is_prime, num_list))
    print("--- შემოწმების შედეგები ---")
    for num, prime in results:
        status = "მარტივია" if prime else "შედგენილია"
        print(f"რიცხვი {num}: {status}")