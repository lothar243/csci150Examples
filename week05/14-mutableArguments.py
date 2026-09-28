"""In this program, we explore the possible problems with passing
a mutable object as an argument"""


def swap_order(my_var):
    """Swaps the order of the first two items in the list"""
    temp = my_var[0]
    my_var[0] = my_var[1]
    my_var[1] = temp


my_list = [1, 2, 3, 4]
print(f"my_list before calling swap_order: {my_list=}")
# 1, 2, 3, 4
swap_order(my_list)
print(f"my_list after calling swap_order: {my_list=}")
# 2, 1, 3, 4

my_tuple = (1, 2, 3, 4)
print(f"my_tuple before calling swap_order: {my_tuple=}")
# 1, 2, 3, 4
swap_order(my_tuple) # error - you can't change a tuple
print(f"my_tuple after calling swap_order: {my_tuple=}")

