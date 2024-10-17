# countdown.py
from time import sleep

def countdown(start):
    print(f"Starting countdown from {start}!")

    while start > 0:
        print(f"{start}...")
        sleep(.5)
        start -= 1  # Decrement the counter

    print("Liftoff!")

def main():
    start = input("Enter a number to start the countdown from: ")

    if start.isdigit():
        countdown(int(start))
    else:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()