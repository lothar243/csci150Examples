# loopDict.py

def iterate_dict():
    student_grade = {
        "Alice": "A",
        "Bob": "B",
        "Charlie": "C",
        "Diana": "A"
    }

    print("Iterating through the dictionary of student grades:")
    for student, grade in student_grade.items():
        print(f"Student: {student}, Grade: {grade}")

if __name__ == "__main__":
    iterate_dict()