#!/usr/bin/env python3
"""
studentGrades.py

Example program that imports tableFormatter.py and uses it to
format a table of student grades.
"""

import tableFormatter  # make sure tableFormatter.py is in the same folder

# Define custom columns (header, width)
GRADE_COLS = [
    ("Name",    20),
    ("Assignment", 15),
    ("Score",   6),
    ("Grade",   6),
    ("Comments", 25),
]

# Example data rows
grade_rows = [
    ("Alice Johnson", "Homework 1", 95, "A", "Excellent work!"),
    ("Bob Smith", "Project", 82, "B", "Good, but could improve formatting."),
    ("Charlie Lee", "Homework 2", 74, "C", "Missed some requirements."),
    ("Dana Brown", "Quiz 1", 100, "A", "Perfect score!"),
    ("Evan Wright", "Homework 1", 67, "D", "Late submission."),
]

# Use the formatter from tableFormat
print(tableFormatter.format_table(grade_rows, cols=GRADE_COLS))
