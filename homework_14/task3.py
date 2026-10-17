"""
Homework 14 - Task 3

collect_people(n) asks the user n times for a first name, last name and
age, then writes everything into "people.csv" using csv.DictWriter.

Example (n = 2):
    ID,first_name,last_name,age
    1,John,Doe,25
    2,Alice,White,30

Age input is validated with try/except to make sure it is a valid integer.
"""

import csv

OUTPUT_FILE = "people.csv"
FIELDNAMES = ["ID", "first_name", "last_name", "age"]


def collect_people(n):
    people = []

    for i in range(1, n + 1):
        print(f"\n--- Person {i} ---")
        first_name = input("Enter first name: ").strip()
        last_name = input("Enter last name: ").strip()

        while True:
            try:
                age = int(input("Enter age: ").strip())
                break
            except ValueError:
                print("Age must be a whole number. Please try again.")

        people.append({
            "ID": i,
            "first_name": first_name,
            "last_name": last_name,
            "age": age,
        })

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(people)

    print(f"\nSaved {n} people to '{OUTPUT_FILE}'.")


if __name__ == "__main__":
    count = int(input("How many people do you want to enter? "))
    collect_people(count)
