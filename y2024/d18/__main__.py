import time

from y2024.d18.solution import Maze

if __name__ == '__main__':
    lines = []
    with open("data", "r") as data_file:
        for line in data_file:
            lines.append(line.rstrip())

    maze = Maze(71, 71, lines)
    print("Part 1:")
    start = time.time()
    print(f"{maze.get_shortest_path_length(1024)} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{maze.get_last_coordinate_before_inescapable()} time: {time.time() - start}s")