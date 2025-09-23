"""Example: Default arguments in a shopping cart"""

def add_item(item_name, quantity=1):
    """Add an item to the cart. Default is 1 item."""
    print(f"Added {quantity} x {item_name} to the cart.")


def calculate_total(price_per_item, quantity=1, discount=0.0):
    """Calculate total cost. Default is 1 item, no discount."""
    total = price_per_item * quantity
    total -= total * discount
    print(f"Total for {quantity} item(s) with {discount*100}% discount: ${total:.2f}")


def checkout(customer_name="Guest", payment_method="cash"):
    """Complete the purchase with default name and payment method."""
    print(f"Checkout complete for {customer_name} using {payment_method}.")


# Demonstration
add_item("Apple")                # default quantity = 1
add_item("Banana", 3)            # overrides default

calculate_total(2.50)            # 1 item, no discount
calculate_total(5.00, 4)         # 4 items, no discount
calculate_total(10.00, 2, 0.1)   # 2 items, 10% discount

checkout()                       # default Guest + cash
checkout("Alice")                # Alice, default cash
checkout("Bob", "credit card")   # Bob, custom payment
