from pprint import pprint

original_matrix = [[1, 2, 3, 1, 2, 3], [4, 5, 6, 7, 4, 3], [7, 8, 9, 6, 1, 4]]

def double_matrix(matrix):
    # create a copy of matrix to be sure not to modify the original
    new_matrix = matrix[:]
    for rowIndex, row in enumerate(matrix):
        for colIndex, value in enumerate(row):
            new_matrix[rowIndex][colIndex] = 2 * value
    return new_matrix

if(__name__ == "__main__"):
    altered_matrix = double_matrix(original_matrix)
    print("The original matrix:")
    pprint(original_matrix, width=30)
    print()
    print("The altered matrix:")
    pprint(altered_matrix, width=30)