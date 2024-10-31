# Print one line at a time, advance by pressing 'enter'.

with open("dracula.txt", 'r') as myfile:
    for line in myfile:
        print(line, end=" ")
        input()

# Problem: the double-spacing is back