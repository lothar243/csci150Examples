def example_with_finally():
    file = None
    try:
        print("Opening file...")
        file = open("somefile.txt", "r")
        print("Reading file...")
        content = file.read()
        print("File content:", content)
    except FileNotFoundError:
        print("File not found!")
    finally:
        print("Cleaning up...")
        if file:
            file.close()  # Ensures this runs only if the file was successfully opened
            print("File closed.")

example_with_finally()