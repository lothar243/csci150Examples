from pprint import pprint

matrix = [[1, 2, 3, 1, 2, 3], [4, 5, 6, 7, 4, 3], [7, 8, 9, 6, 1, 4]]

print("pprint with width = 30")
pprint (matrix, width=30) # the low width forces pprint ot use multiple lines

print()
print("pprint with compact=True")
pprint (matrix, compact=True)

print()
print("Manually defining how it is printed")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()