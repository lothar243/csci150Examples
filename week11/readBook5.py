# Check to see if the input is a 'q', which will break the loop

with open("dracula.txt", 'r') as myfile:
    for line in myfile:
        print(line.strip(), end=" ")
        command = input()
        if command == 'q':
            break

# Problem: You have to start from the beginning every time