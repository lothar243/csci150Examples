def split_check(amount, num_people, tax_percentage, tip_percentage):
    print(f"amount = {amount}, "
    + "num_people = {num_people}, "
    + "tax_percentage = {tax_percentage}, "
    + "tip_percentage = {tip_percentage}")

split_check(125.00, tip_percentage=0.15, num_people=2, tax_percentage=0.095)

# putting keyword arguments before positional arguments generates an error
# split_check(tip_percentage=0.15, num_people=2, tax_percentage=0.095, 125.00)

split_check(tip_percentage=0.15, num_people=2, tax_percentage=0.095, amount=125.00)