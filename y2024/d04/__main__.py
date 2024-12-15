import time

from y2024.d04.ceres_cearch import CeresSearch

if __name__ == '__main__':
    puzzle = []
    with open("data", "r") as data_file:
        for line in data_file:
            puzzle.append(line.rstrip())

    ceres_search = CeresSearch(puzzle)
    print("Part 1:")
    start = time.time()
    print(f"{ceres_search.get_occurrence_count("XMAS")} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{ceres_search.get_x_mas_occurrence_count()} time: {time.time() - start}s")