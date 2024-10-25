import random

numbers = []
for _ in range(10):
    numbers.append(random.randrange(20))

print(numbers)


numbers = [random.randrange(20) for _ in range(10)]

print(numbers)
