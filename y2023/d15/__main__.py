import time
from y2023.d15.lenslibrary import LensLibrary

if __name__ == '__main__':
    initialization_sequence = []
    with open("data", "r") as data_file:
        for line in data_file:
            initialization_sequence.append(line.rstrip())

    print("What is the sum of the results?")
    start = time.time()
    print(f"{LensLibrary.get_hash_initialization_sequence(initialization_sequence[0])} time: {time.time() - start}s")
