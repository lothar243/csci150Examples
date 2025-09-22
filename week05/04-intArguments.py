"""Example: Passing numbers and strings to functions"""

def print_score(round_1_points, round_2_points):
    total_points = round_1_points + round_2_points
    average_points = total_points / 2
    print(f"An average of {average_points}, resulting in a total of {total_points} points.")


# Demonstrate the use of parameters in functions
user_1_name = input("What is the name of the first user? ")
user_2_name = input("What is the name of the second user? ")

print("------- Running game... -------")
print(f"Username: {user_1_name}")
print_score(10, 5)

print(f"Username: {user_2_name}")
print_score(42, 8)
