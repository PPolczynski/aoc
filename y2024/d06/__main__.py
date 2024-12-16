import time

from y2024.d06.solution import Maze

if __name__ == '__main__':
    maze = []
    with open("data", "r") as data_file:
        for line in data_file:
            maze.append(line.rstrip())

    guard_gallivant = Maze(maze)
    print("Part 1:")
    start = time.time()
    print(f"{guard_gallivant.get_guard_move_count()} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{guard_gallivant.get_possible_loop_count()} time: {time.time() - start}s")