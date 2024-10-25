my_dict = {"a": 1, "b": 2, "c": 3}

print(f"Before: {my_dict}")

# Trying to remove an item while iterating over the dictionary
for key in my_dict:
    if key == "b":
        del my_dict[key]  # This will raise a RuntimeError

print(f"After: {my_dict}")

# Expected output:
# Before: {'a': 1, 'b': 2, 'c': 3}
# After: {'a': 1, 'c': 3}

# To safely modify a dictionary while iterating, work on a copy of the dictionary’s keys or items:
# for key in list(my_dict.keys()):