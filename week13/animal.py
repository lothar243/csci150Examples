class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def bark(self):
        print("Woof!")

my_dog = Dog()
my_dog.eat()  # Inherited from Animal class
my_dog.bark()  # Defined in Dog class