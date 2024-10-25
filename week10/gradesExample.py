# Nested dictionary representing students and their course grades
students_grades = {
    "Alice": {
        "Math": 90,
        "Science": 85,
        "History": 88
    },
    "Bob": {
        "Math": 78,
        "Science": 82,
        "History": 80
    },
    "Charlie": {
        "Math": 92,
        "Science": 88,
        "History": 91
    }
}

# Accessing a student's grades
print(f"Alice's grades: {students_grades['Alice']}")

# Accessing a specific grade (Charlie's grade in Science)
print(f"Charlie's Science grade: {students_grades['Charlie']['Science']}")

# Adding a new course for Bob
students_grades["Bob"]["Art"] = 89

# Updating a grade (Alice's History grade)
students_grades["Alice"]["History"] = 90

# Displaying the updated dictionary
print("\nUpdated grades:")
for student, grades in students_grades.items():
    print(f"{student}: {grades}")
