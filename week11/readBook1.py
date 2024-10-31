# First step - open file, read lines, print lines

with open("dracula.txt", 'r') as myfile:
    for line in myfile:
        print(line)

# problem: text is double-spaced