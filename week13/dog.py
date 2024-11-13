import json

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, a {self.age}-year-old dog"

my_dog = Dog("Buddy", 3)

print(my_dog)
