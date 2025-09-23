price = float(input("Original price: "))
tax_rate = float(input("Tax amount: "))
tax_amount = price * tax_rate / 100
total = price + tax_amount

print("The amount of tax is ${:.2f} and the total amount comes to ${:.2f}".format(tax_amount, total))
