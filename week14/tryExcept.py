try:
    userInput = int(input("Enter a number: "))
except ValueError as e:
    print("There was an error: " + str(e))