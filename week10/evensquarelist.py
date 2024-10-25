# Original list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using list comprehension to create a new list of squares of even numbers
squares_of_even = [x**2 for x in numbers if x % 2 == 0]

print(squares_of_even)
