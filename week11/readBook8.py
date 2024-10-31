# The file is opened and the current progress line is read
progress_file_name = "progress.txt"
with open(progress_file_name, "r") as progressFile:
    progress_line = int(progressFile.readline())

with open("dracula.txt", 'r') as myfile:
    for lineNumber, lineText in enumerate(myfile):
        # Fast forward to get to the current line
        if lineNumber < progress_line:
            continue
        print(lineText.strip(), end=" ")
        command = input()
        if command == 'q':
            print(f"Quitting at line number {lineNumber}, we will resume from here next time")
            with open(progress_file_name, 'w') as progress_file:
                progress_file.write(str(lineNumber))
            break

# Problem: You can't start reading the book (the file doesn't exist to begin with)