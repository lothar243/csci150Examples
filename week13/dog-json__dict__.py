import json

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_dog = Dog("Buddy", 3)

# Using the __dict__ attribute to convert object to a dictionary
dog_json = json.dumps(my_dog.__dict__)
print(dog_json)  # Output: {"name": "Buddy", "age": 3}
