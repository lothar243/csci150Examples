# infiniteLoopExample.py

def count_down():
    num = 5
    print("Starting countdown...")

    # This loop will run infinitely because `num` is never updated
    while num > 0:
        print(f"Counting down: {num}")
        num = num - 1

    print("Countdown finished!")

if __name__ == "__main__":
    count_down()