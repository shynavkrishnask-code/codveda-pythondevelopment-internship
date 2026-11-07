"""
Level 1 - Task 2: Number Guessing Game
The computer picks a number between 1 and 100; the player has a limited
number of attempts to guess it.
"""

import random

LOWER = 1
UPPER = 100
MAX_ATTEMPTS = 7


def get_guess(attempts_left):
    """Ask for a guess and validate it."""
    while True:
        raw = input(f"Enter your guess ({LOWER}-{UPPER}) [{attempts_left} attempts left]: ").strip()
        try:
            guess = int(raw)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        if not LOWER <= guess <= UPPER:
            print(f"Please guess a number between {LOWER} and {UPPER}.")
            continue
        return guess


def play_round():
    secret = random.randint(LOWER, UPPER)
    attempts_used = 0

    print(f"\nI'm thinking of a number between {LOWER} and {UPPER}.")
    print(f"You have {MAX_ATTEMPTS} attempts. Good luck!\n")

    while attempts_used < MAX_ATTEMPTS:
        guess = get_guess(MAX_ATTEMPTS - attempts_used)
        attempts_used += 1

        if guess < secret:
            print("Too low!\n")
        elif guess > secret:
            print("Too high!\n")
        else:
            print(f"Correct! You guessed it in {attempts_used} attempt(s).")
            return

    print(f"Out of attempts! The number was {secret}.")


def main():
    print("=== Number Guessing Game ===")
    while True:
        play_round()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
