def example_without_finally():
    try:
        print("Opening file...")
        file = open("somefile.txt", "r")
        print("Reading file...")
        content = file.read()
        print("File content:", content)
    except FileNotFoundError:
        print("File not found!")
    
    # Trying to close the file here (outside the try-except block)
    print("Closing file...")
    if file:
        file.close()
        print("File closed.")

example_without_finally()