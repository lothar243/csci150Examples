numbers = [5, 8, 4, 6, 0, 7, 2, 3, 9, 1]

## Why doesn't the following work? ##
print(numbers)

print("Removing all items from the list that are less than 5")
for i, val in enumerate(numbers):
    while val < 5:
        numbers.pop(i)
        val = numbers[i]

print(numbers)




# expected output
# [5, 8, 4, 6, 0, 7, 2, 3, 9, 1]
# [5, 8, 6, 7, 3, 9]
# if sorted: [1, 3, 5, 6, 7, 8, 9]
