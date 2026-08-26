import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Generate a random number between 1 and 100
answer = random.randint(1, 100)

# Choose difficulty
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

# Set attempts based on difficulty
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
else:
    print("Invalid difficulty. Please restart the game.")
    exit()

# Game loop
while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))

    if guess == answer:
        print(f"You got it! The answer was {answer}.")
        break

    elif guess > answer:
        print("Too high.")
        print("Guess again.")

    else:
        print("Too low.")
        print("Guess again.")

    attempts -= 1

    if attempts == 0:
        print(f"You've run out of guesses. The answer was {answer}.")
