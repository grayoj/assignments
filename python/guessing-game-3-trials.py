# Gerald Maduabuchi, 2023
# Create a guessing game program that will tell the user to get the particular number after 3 trials.

# Import random module generators
import random


# Number of attemots
attempts = 3

# Generate a random number for the variable number between 1 and 20
number = random.randint(1, 20)


# For loop to initialise guessing game logic
for i in range(attempts):
    guess = int(input("Guess a number between 1 and 10: "))

    # IF/ELSE loop logic to determine if the guess was correct
    if guess == number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Sorry, that was incorrect.")
        if i == 2:
            print(f"The number was {number}.")
