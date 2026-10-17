"""
Homework 14 - Task 2

Reads "persons.txt" (format: "Full Name, age, city" - one person per line)
and splits the people into two new text files, keeping the original
formatting:

    - under_50.txt  -> everyone younger than 50
    - over_50.txt   -> everyone 50 or older
"""

INPUT_FILE = "persons.txt"
UNDER_50_FILE = "under_50.txt"
OVER_50_FILE = "over_50.txt"


def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file if line.strip()]

    under_50 = []
    over_50 = []

    for line in lines:
        # Format: "Full Name, age, city"
        parts = line.split(",")
        age = int(parts[1].strip())

        if age < 50:
            under_50.append(line)
        else:
            over_50.append(line)

    with open(UNDER_50_FILE, "w", encoding="utf-8") as file:
        file.write("\n".join(under_50) + "\n")

    with open(OVER_50_FILE, "w", encoding="utf-8") as file:
        file.write("\n".join(over_50) + "\n")

    print(f"Saved {len(under_50)} people under 50 to '{UNDER_50_FILE}'.")
    print(f"Saved {len(over_50)} people 50 or older to '{OVER_50_FILE}'.")


if __name__ == "__main__":
    main()
