"""goes through multiple sandwiches and prints their contents"""


def sandwich(bread, meat, **kwargs):
    """prints the contents of the sandwich"""
    print('{} on {}'.format(meat, bread))
    for category, extra in kwargs.items():
        print('   {}: {}'.format(category, extra))


sandwich('sourdough', 'turkey', sauce='mayo')
sandwich('wheat', 'ham', sauce1='mustard', veggie1='tomato', veggie2='lettuce')
