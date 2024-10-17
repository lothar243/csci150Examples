# enumerateExample.py

def demonstrate_enumerate():
    fruits = ["apple", "banana", "cherry", "date"]

    print("Iterating through the list with indexes using enumerate:")
    for index, fruit in enumerate(fruits):
        print(f"Index: {index}, Fruit: {fruit}")

if __name__ == "__main__":
    demonstrate_enumerate()