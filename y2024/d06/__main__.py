import time

from y2024.d06.solution import Maze

if __name__ == '__main__':
    maze_lines = []
    with open("data", "r") as data_file:
        for line in data_file:
            maze_lines.append(line.rstrip())

    maze = Maze(maze_lines)
    print("Part 1:")
    start = time.time()
    print(f"{maze.get_guard_move_count()} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{maze.get_possible_loop_count()} time: {time.time() - start}s")