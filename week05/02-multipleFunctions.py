# Example: Demonstrating how functions facility code reuse
import random


def say_hello():
    print("Hello there!")

def roll_dice():
    number = random.randint(1, 6)
    print("You rolled a", number)

def show_line():
    print("--------------------")


# Main program - call the functions that have been defined
say_hello()
roll_dice()
roll_dice()
show_line()

say_hello()
show_line()
roll_dice()
say_hello()
