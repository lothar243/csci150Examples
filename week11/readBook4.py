# Remove the whitespace surrounding each line

with open("dracula.txt", 'r') as myfile:
    for line in myfile:
        print(line.strip(), end=" ")
        input()

# Problem: you can't exit the book midway