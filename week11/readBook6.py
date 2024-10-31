# Added a way to specify a line to resume from

progress_line = 15

with open("dracula.txt", 'r') as myfile:
    for lineNumber, lineText in enumerate(myfile):
        # Fast forward to get to the current line
        if lineNumber < progress_line:
            continue
        print(lineText.strip(), end=" ")
        command = input()
        if command == 'q':
            break

# Problem: The progress line requires altering the source code