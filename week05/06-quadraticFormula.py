"""Showing a function that returns a value"""
import math


def quadratic_solutions(a, b, c):
    """Given the arguments a, b, and c, gives the
    solutions to the equation ax^2 + bx + c = 0
    """
    determinant = b ** 2 - 4 * a * c
    return ((-b + math.sqrt(determinant)) / (2 * a),
            (-b - math.sqrt(determinant)) / (2 * a))


sol1, sol2 = quadratic_solutions(1, -3, 0)
print("The first solution is:", sol1)
print("The second solution is:", sol2)
#print(quadratic_solutions.__doc__)
help(quadratic_solutions)
