import random

# Define the heuristic function to determine the distance between the guessed number and the target number
def heuristic(guess, target):
    return abs(guess - target)

# Define the target number and the maximum number of guesses
target = random.randint(1, 100)
max_guesses = 10

# Initialize the guess counter
num_guesses = 0

# Game loop
while num_guesses < max_guesses:
    # Get user's guess
    guess = int(input("Enter your guess (1-100): "))
    num_guesses += 1

    # Check if the guess is correct
    if guess == target:
        print("Congratulations! You guessed the correct number in", num_guesses, "guesses.")
        break
    else:
        # Provide feedback on the guess
        if guess < target:
            print("Higher! Guess again.")
        else:
            print("Lower! Guess again.")

    # Calculate the heuristic value for the next guess
    heuristic_value = heuristic(guess, target)

    # Print the heuristic value for the next guess
    print("Heuristic value for next guess:", heuristic_value)

    # End the game if maximum guesses are reached
    if num_guesses == max_guesses:
        print("Sorry, you've reached the maximum number of guesses. The target number was:", target)
