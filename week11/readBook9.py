# Check to ensure the progress file exists before opening it
import os

progress_file_name = "progress.txt"
# Check to see if a progress file exists. If it does, read the value so we can resume from that line
if os.path.isfile(progress_file_name):
    with open(progress_file_name, "r") as progressFile:
        progress_line = int(progressFile.readline())
else:
    # The progress file doesn't previously exist, so start from the beginning
    progress_line = 0

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

# Problem: When you get to the end of the book, you can't start reading it again
# Further features:
# Delete the progress file when you reach the end of the book
# Allow user to select the book they are reading
# Keep track of progress in several different books
# etc...