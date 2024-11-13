import json

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def encode_custom(obj):
    if isinstance(obj, Dog):
        return obj.__dict__  # or return a custom dict representation
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

my_dog = Dog("Buddy", 3)

# Use the default parameter to handle custom objects
dog_json = json.dumps(my_dog, default=encode_custom)
print(dog_json)  # Output: {"name": "Buddy", "age": 3}
