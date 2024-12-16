import time

from y2024.d11.solution import BlinkingStones

if __name__ == '__main__':
    lines = []
    with open("data", "r") as data_file:
        for line in data_file:
            lines.append(line.rstrip())

    print("Part 1:")
    start = time.time()
    print(f"{BlinkingStones.count_stones(lines[0], 25)} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{BlinkingStones.count_stones(lines[0], 75)} time: {time.time() - start}s")
