"""Example: Passing arguments to functions"""

def greet(name):
    print(f"Hello, {name}!")


def cheer(verb, adverb):
    print(f"You are {verb} {adverb}!")


def print_three_times(text):
    print(text)
    print(text)
    print(text)


# Demonstrate the use of arguments in functions
username = input("What is your name? ")
greet(username)
cheer("doing", "great")
print_three_times("Hip hip hooray")
print_three_times("------------")