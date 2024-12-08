import time

from y2023.d10.pipe_maze import PipeMaze

if __name__ == '__main__':
    maze = []
    with open("data", "r") as data_file:
        for line in data_file:
            maze.append(line.rstrip())

    pipe_maze = PipeMaze(maze)
    print("How many steps along the loop does it take to get from the starting position to the point farthest from the starting position?")
    start = time.time()
    print(f"{pipe_maze.get_furthest_step()} time: {time.time() - start}s")
    print("How many tiles are enclosed by the loop?")
    start = time.time()
    print(f"{pipe_maze.get_enclosed_tile_count()} time: {time.time() - start}s")
