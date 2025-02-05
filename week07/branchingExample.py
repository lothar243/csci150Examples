numStudents = int(input("Please enter the number of students registered for the class: "))

print()
if numStudents > 10:
    print("There are at least 10 students in the class")
    print("The class will start next Sunday")
else:
    print("There are not yet enough students registered for the class")
    print("We will delay starting the class until more register")

print("For more information, please ask email info@example.com")
