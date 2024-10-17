# weekdayQuestion.py

def ask_weekday():
    valid_weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    day = input("Please enter a weekday (e.g., Monday): ").strip().lower()

    # Keep asking while the input is not a valid weekday
    while day not in valid_weekdays:
        print("Invalid input. Please enter a valid weekday.")
        day = input("Please enter a weekday (e.g., Monday): ").strip().lower()
    
    print(f"You entered a valid day: {day.capitalize()}")

# Call the function to execute the program
if __name__ == "__main__":
    ask_weekday()