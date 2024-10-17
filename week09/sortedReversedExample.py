# sortedReversedExample.py

def demonstrate_sorted_reversed():
    numbers = [5, 2, 9, 1, 7]

    # Using sorted() to iterate in ascending order
    print("Iterating in ascending order (sorted):")
    for num in sorted(numbers):
        print(num)

    # Using sorted() with reverse=True to iterate in descending order
    print("\nIterating in descending order (sorted in reverse):")
    for num in sorted(numbers, reverse=True):
        print(num)

    # Using reversed() to iterate in reverse of the original order
    print("\nIterating in reverse order of the original list:")
    for num in reversed(numbers):
        print(num)

if __name__ == "__main__":
    demonstrate_sorted_reversed()