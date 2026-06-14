import random
secret_number = random.randint(1, 100)
lives = 5
print("--- Guessing Game ---")
print("program has chosen a random number between 1 and 100. Try to guess it in 5 tries.")
while lives > 0:  
    guess = int(input(f"\nenter your guess (lives - {lives}): "))
    if guess == secret_number:
        print("\nwell done. you guessed the number!")
        break       
    elif guess < secret_number:
        print("chosen number is greater than your guess.")
        lives -= 1  
    else: 
        print("chosen number is less than your guess.")
        lives -= 1 
if lives == 0:
    print("\nyou lost.")
    print(f"chosen number was{secret_number}")