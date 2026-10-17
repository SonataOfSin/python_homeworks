"""
Homework 14 - Task 1

Repeatedly asks the user for a first name and a last name and writes them,
numbered, to "names.txt" - one person per line. The program stops as soon
as the user types "stop" instead of a first name.

Example:
    Enter your first name: Otar
    Enter your last name: Tumanishvili
    Enter your first name: Nika
    Enter your last name: Papaskiri
    Enter your first name: stop

Resulting file (names.txt):
    1. Otar Tumanishvili
    2. Nika Papaskiri
"""

OUTPUT_FILE = "names.txt"


def main():
    counter = 1
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        while True:
            first_name = input("Enter your first name: ").strip()
            if first_name.lower() == "stop":
                break

            last_name = input("Enter your last name: ").strip()

            file.write(f"{counter}. {first_name} {last_name}\n")
            file.flush()
            counter += 1

    print(f"Done! Names were saved to '{OUTPUT_FILE}'.")


if __name__ == "__main__":
    main()
