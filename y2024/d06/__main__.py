import time

from y2024.d06.guard_gallivant import GuardGallivant

if __name__ == '__main__':
    maze = []
    with open("data", "r") as data_file:
        for line in data_file:
            maze.append(line.rstrip())

    guard_gallivant = GuardGallivant(maze)
    print("How many distinct positions will the guard visit before leaving the mapped area?")
    start = time.time()
    print(f"{guard_gallivant.get_guard_move_count()} time: {time.time() - start}s")
    print("How many different positions could you choose for this obstruction?")
    start = time.time()
    print(f"{guard_gallivant.get_possible_loop_count()} time: {time.time() - start}s")