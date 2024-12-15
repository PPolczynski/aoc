import time

from y2024.d03.mull_it_over import MullItOver

if __name__ == '__main__':
    corrupted_memory = []
    with open("data", "r") as data_file:
        for line in data_file:
            corrupted_memory.append(line.rstrip())

    print("Part 1:")
    start = time.time()
    print(f"{sum([MullItOver.get_sum_of_multiplications(line) for line in corrupted_memory])} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{MullItOver.get_sum_of_multiplications_conditional("".join(corrupted_memory))} time: {time.time() - start}s")