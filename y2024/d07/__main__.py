import time

from y2024.d07.solution import Solution

if __name__ == '__main__':
    data = []
    with open("data", "r") as data_file:
        for line in data_file:
            target, values = line.rstrip().split(": ")
            data.append((int(target), list(map(int, values.split(" ")))))

    bridge_repair = Solution()
    print("Part 1:")
    start = time.time()
    print(f"{bridge_repair.get_sum_valid_targets(data)} time: {time.time() - start}s")
    print("Part 1: implemented based on found solution")
    start = time.time()
    print(f"{bridge_repair.get_sum_valid_found(data, False)} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{bridge_repair.get_sum_valid_targets_with_concat(data)} time: {time.time() - start}s")
    print("Part 2: implemented based on found solution")
    start = time.time()
    print(f"{bridge_repair.get_sum_valid_found(data, True)} time: {time.time() - start}s")