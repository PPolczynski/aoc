import time

from y2024.d14.solution import Robots

if __name__ == '__main__':
    lines = []
    with open("data", "r") as data_file:
        for line in data_file:
            lines.append(line.rstrip())

    robots = Robots(lines, 101, 103)
    print("Part 1:")
    start = time.time()
    robots.pass_time(100)
    print(f"{robots.get_safety_factor()} time: {time.time() - start}s")
    robots = Robots(lines, 101, 103)
    print("Part 2:")
    # robots.search_for_christmas_tree_manual()
    # after 1000 button presses time to move to smarter solution :)
    robots.search_for_christmas_tree(3)
    # 3 is the first value for which no noise is detected
