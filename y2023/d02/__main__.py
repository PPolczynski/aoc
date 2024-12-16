import time

from y2023.d02.solution import CubeGame

if __name__ == '__main__':
    games = []
    with open("data", "r") as data_file:
        for line in data_file:
            games.append(line.rstrip())
    cube_game = CubeGame([("red", 12), ("green", 13), ("blue", 14)])
    print("Part 1:")
    start = time.time()
    print(f"{cube_game.get_sum_possible_id(games)} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{cube_game.get_sum_of_power(games)} time: {time.time() - start}s")