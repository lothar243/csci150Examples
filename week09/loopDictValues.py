# valuesExample.py

def iterate_values():
    student_grades = {
        "Alice": "A",
        "Bob": "B",
        "Charlie": "C",
        "Diana": "A"
    }

    print("Iterating through the values of the dictionary:")
    for grade in student_grades.values():
        print(f"Grade: {grade}")

if __name__ == "__main__":
    iterate_values()