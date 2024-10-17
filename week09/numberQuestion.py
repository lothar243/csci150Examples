# numberQuestion.py

def ask_number():
    user_input = input("Please enter a number: ")

    # Keep asking while the input is not a valid number
    while not user_input.isdigit():
        print("Invalid input. Please enter a valid number.")
        user_input = input("Please enter a number: ")
    
    print(f"You entered a valid number: {user_input}")

# Call the function to execute the program
if __name__ == "__main__":
    ask_number()