"""goes through multiple sandwiches and prints their contents"""


def sandwich(bread, meat, **toppings):
    """prints the contents of the sandwich"""
    print(f'{meat} on {bread}, toppings: ', toppings)


sandwich('sourdough', 'turkey', sauce='mayo')
sandwich('wheat', 'ham', sauce1='mustard', veggie1='tomato', veggie2='lettuce')
