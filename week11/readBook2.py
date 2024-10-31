# lines have their own newlines when read, so don't add one with print

with open("dracula.txt", 'r') as myfile:
    for line in myfile:
        print(line, end=" ")

# problem: text displays all at once, user should be able to display one line at at time