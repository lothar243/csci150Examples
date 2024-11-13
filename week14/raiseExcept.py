try:
    print("We will divide $100 evenly between a certain number of people")
    numPeople = int(input("Please enter the number of people "))
    if(numPeople <= 0):
        raise ValueError
    valuePerPerson = 100 / numPeople
    print(f"Each person should get ${valuePerPerson:.2f}")
except ValueError:
    print("You need to specify a number of people")
except:
    print("You did something I didn't expect")