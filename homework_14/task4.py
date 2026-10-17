"""
Homework 14 - Task 4

Reads "students.csv" and splits students by Grade using csv.DictReader /
csv.DictWriter:

    - failed_students.csv -> Grade < 50
    - passed_students.csv -> Grade > 50   (>= 50 is treated as passed)
"""

import csv

INPUT_FILE = "students.csv"
FAILED_FILE = "failed_students.csv"
PASSED_FILE = "passed_students.csv"


def main():
    with open(INPUT_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        rows = list(reader)

    failed = [row for row in rows if int(row["Grade"]) < 50]
    passed = [row for row in rows if int(row["Grade"]) >= 50]

    with open(FAILED_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(failed)

    with open(PASSED_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(passed)

    print(f"Saved {len(failed)} failed students to '{FAILED_FILE}'.")
    print(f"Saved {len(passed)} passed students to '{PASSED_FILE}'.")


if __name__ == "__main__":
    main()
