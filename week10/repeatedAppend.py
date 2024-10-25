import timeit

def append_with_loop():
    result = []
    for i in range(10000):
        result.append(i**2)

def append_with_comprehension():
    result = [i**2 for i in range(10000)]

if __name__ == "__main__":
    loop_time = timeit.timeit(append_with_loop, number=1000)
    comprehension_time = timeit.timeit(append_with_comprehension, number=1000)

    print(f"{loop_time=}")
    print(f"{comprehension_time=}")

    percent = loop_time / comprehension_time * 100
    print(f"Appending with a loop took {percent:.2f}% the time that list comprehension took")
