try:
    print("We will divide $100 evenly between a certain number of people")
    numPeople = int(input("Please enter the number of people "))
    valuePerPerson = 100 / numPeople
    print(f"Each person should get ${valuePerPerson:.2f}")
except ValueError:
    print("You didn't enter a number")
except ZeroDivisionError:
    print("You can't divide this among 0 people")
except:
    print("You did something I didn't expect")