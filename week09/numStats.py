# numStats.py

def collect_numbers():
    numbers = []

    while True:
        user_input = input("Enter a number (or 'q' to quit): ").strip().lower()

        if user_input == 'q':
            break
        elif user_input.isdigit():
            numbers.append(int(user_input))
        else:
            print("Invalid input. Please enter a valid number or 'q' to quit.")

    return numbers

def display_statistics(numbers):
    if not numbers:
        print("No numbers were entered.")
    else:
        count = len(numbers)
        total_sum = sum(numbers)
        average = total_sum / count
        minimum = min(numbers)
        maximum = max(numbers)

        print("\nStatistics:")
        print(f"Count: {count}")
        print(f"Sum: {total_sum}")
        print(f"Average: {average:.2f}")
        print(f"Minimum: {minimum}")
        print(f"Maximum: {maximum}")

def main():
    print("Welcome to the Number Statistics Program!")
    numbers = collect_numbers()
    display_statistics(numbers)

if __name__ == "__main__":
    main()