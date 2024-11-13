import json

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age
        }

my_dog = Dog("Buddy", 3)

# Convert object to dictionary, then to JSON
dog_json = json.dumps(my_dog.to_dict())
print(dog_json)  # Output: {"name": "Buddy", "age": 3}