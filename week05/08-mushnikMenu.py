"""Demonstrate functions calling other functions"""


def print_menu(shop_name, item_list, price_list):
    """Print a nicely formatted menu with all the items and prices"""
    print("*" * 35)
    print(f"*** {shop_name:^27} ***")
    print("*" * 35)
    for index in range(len(item_list)):
        print_menu_item(item_list[index], price_list[index])
    print("*" * 35)

def print_menu_item(item_name, item_price):
    """Print an item and its price, formatted to fit with the menu"""
    price_string = f"${item_price:.2f}"
    print(f"* {item_name:<24} {price_string:>6} *")


store_name = "Mushnik's Flower Shop"
item_list = ["Tulip", "Rose", "Venus Fly Trap"]
price_list = [4.99, 5.99, 14.99]

print_menu(store_name, item_list, price_list)
