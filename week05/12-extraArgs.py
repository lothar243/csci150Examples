def sandwich(bread, meat, *args):
    print('{} on {}'.format(meat, bread), end=' ')
    if len(args) > 0:
        print('with', end=' ')
    for extra in args:
        print(extra, end=' ')
    print('')


sandwich('sourdough', 'turkey', 'mayo')
sandwich('wheat', 'ham', 'mustard', 'tomato', 'lettuce')
