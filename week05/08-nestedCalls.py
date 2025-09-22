"""Demonstrate nested function calls and the importance of return values"""


def reverse_list(input_list):
    """Given a list, returns a list with reversed order"""
    output_list = []
    for item in reversed(input_list):
        output_list.append(item)
    return output_list


def sort_list(input_list):
    output_list = []
    for item in sorted(input_list):
        output_list.append(item)
    return output_list


unsorted_list = [2, 5, 1, 3, 7, 4]

print("Original list: " + str(unsorted_list))
print("Sorted list: " + str(sort_list(unsorted_list)))
print("Reversed list: " + str(reverse_list(unsorted_list)))
print("Reverse sorted list: " + str(reverse_list(sort_list(unsorted_list))))
