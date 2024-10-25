matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"{matrix=}")
flat_list = [item for sublist in matrix for item in sublist]
print(f"{flat_list=}")