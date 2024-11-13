import json

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class DogEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Dog):
            return {"name": obj.name, "age": obj.age}
        # Call the base class's default method for other types
        return super().default(obj)

my_dog = Dog("Buddy", 3)

# Use the custom encoder to convert object to JSON
dog_json = json.dumps(my_dog, cls=DogEncoder)
print(dog_json)  # Output: {"name": "Buddy", "age": 3}
