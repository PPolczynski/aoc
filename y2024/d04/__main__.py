from y2024.d04.ceres_cearch import CeresSearch

if __name__ == '__main__':
    puzzle = []
    with open("data", "r") as data_file:
        for line in data_file:
            puzzle.append(line.rstrip())

    ceres_search = CeresSearch(puzzle)
    print("How many times does XMAS appear?")
    print(ceres_search.get_occurrence_count("XMAS"))
    print("How many times does an X-MAS appear?")
    print(ceres_search.get_x_mas_occurrence_count())