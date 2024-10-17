# loopDictKeys.py

def iterate_keys():
    student_grades = {
        "Alice": "A",
        "Bob": "B",
        "Charlie": "C",
        "Diana": "A"
    }

    print("Iterating through the keys of the dictionary:")
    for student in student_grades.keys():
        print(f"Student: {student}")

if __name__ == "__main__":
    iterate_keys()