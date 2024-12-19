import time

from y2024.d19.solution import Onsen

if __name__ == '__main__':
    lines = []
    with open("data", "r") as data_file:
        for line in data_file:
            lines.append(line.rstrip())

    onsen = Onsen(lines)
    print("Part 1:")
    start = time.time()
    print(f"{onsen.get_possible_designs_count()} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{onsen.get_all_possible_designs_count()} time: {time.time() - start}s")