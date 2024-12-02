from y2023.d02.cube_conundrum import CubeConundrum

if __name__ == '__main__':
    games = []
    with open("data", "r") as data_file:
        for line in data_file:
            games.append(line.rstrip())
    cube_conundrum = CubeConundrum([("red", 12), ("green", 13), ("blue", 14)])
    print("What is the sum of the IDs of those games?")
    print(cube_conundrum.get_sum_possible_id(games))
    print("What is the sum of the power of these sets?")
    print(cube_conundrum.get_sum_of_power(games))