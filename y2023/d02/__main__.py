import time

from y2023.d02.cube_conundrum import CubeConundrum

if __name__ == '__main__':
    games = []
    with open("data", "r") as data_file:
        for line in data_file:
            games.append(line.rstrip())
    cube_conundrum = CubeConundrum([("red", 12), ("green", 13), ("blue", 14)])
    print("Part 1:")
    start = time.time()
    print(f"{cube_conundrum.get_sum_possible_id(games)} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{cube_conundrum.get_sum_of_power(games)} time: {time.time() - start}s")