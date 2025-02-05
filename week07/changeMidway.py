# A demonstration of braching

x = int(input("What is the value of x? "))

if x > 4:
    print("The value of x was greater than 4")
    x = 0
    print("It has now been set back to zero")
else:
    print("The value was not greater than 4")
    x = 10
    print("It has been increased")

print("The new value of x is {}".format(x))
