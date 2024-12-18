import time

from y2024.d17.solution import Computer

if __name__ == '__main__':
    lines = []
    with open("data", "r") as data_file:
        for line in data_file:
            lines.append(line.rstrip())

    computer = Computer(lines)
    print("Part 1:")
    start = time.time()
    print(f"{','.join(map(str, computer.run()))} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{computer.get_a_returning_copy()[0]} time: {time.time() - start}s")