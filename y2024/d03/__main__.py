import time

from y2024.d03.solution import Solution

if __name__ == '__main__':
    corrupted_memory = []
    with open("data", "r") as data_file:
        for line in data_file:
            corrupted_memory.append(line.rstrip())

    print("Part 1:")
    start = time.time()
    print(f"{sum([Solution.get_sum_of_multiplications(line) for line in corrupted_memory])} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{Solution.get_sum_of_multiplications_conditional(''.join(corrupted_memory))} time: {time.time() - start}s")