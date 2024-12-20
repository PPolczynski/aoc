import time

from y2024.s20.solution import Maze

if __name__ == '__main__':
    lines = []
    with open("data", "r") as data_file:
        for line in data_file:
            lines.append(line.rstrip())

    maze = Maze(lines, 2)
    print("Part 1:")
    start = time.time()
    print(f"{maze.get_cheats_count(100)} time: {time.time() - start}s")
    # print("Part 2:")
    # start = time.time()
    # print(f"{} time: {time.time() - start}s")