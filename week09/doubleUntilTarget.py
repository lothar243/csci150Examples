# doubleUntilTarget.py

def double_until_target(num, target):
    print(f"Starting with {num}. Doubling until we reach or exceed {target}.")

    while num < target:
        print(f"Current value: {num}")
        num *= 2

    print(f"Finished! The number {num} has reached or exceeded the target {target}.")

def main():
    startingNumber = int(input("Please input a starting number: "))
    target = int(input("Please enter a target number: "))

    double_until_target(startingNumber, target)

if __name__ == "__main__":
    main()