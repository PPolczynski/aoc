import time

from y2024.d14.solution import Robots

if __name__ == '__main__':
    robots = []
    with open("data", "r") as data_file:
        for line in data_file:
            robots.append(line.rstrip())

    restroom_redoubt = Robots(robots, 101, 103)
    print("Part 1:")
    start = time.time()
    restroom_redoubt.pass_time(100)
    print(f"{restroom_redoubt.get_safety_factor()} time: {time.time() - start}s")
    restroom_redoubt = Robots(robots, 101, 103)
    print("Part 2:")
    # restroom_redoubt.search_for_christmas_tree_manual()
    # after 1000 button presses time to move to smarter solution :)
    restroom_redoubt.search_for_christmas_tree(3)
    # 3 is the first value for which no noise is detected
