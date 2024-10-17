# guessingGame.py
import random

def play_game():
    number_to_guess = random.randint(1, 10)
    guess = None

    print("I'm thinking of a number between 1 and 10.")

    while guess != number_to_guess:
        guess = input("Take a guess: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)

        if guess < number_to_guess:
            print("Too low, try again.")
        elif guess > number_to_guess:
            print("Too high, try again.")
        else:
            print(f"Correct! The number was {number_to_guess}.")

def ask_to_play_again():
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    return play_again == "yes"

def main():
    print("Welcome to the Guessing Game!")
    
    while True:
        play_game()
        
        if not ask_to_play_again():
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()