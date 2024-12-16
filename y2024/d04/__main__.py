import time

from y2024.d04.solution import WordPuzzle

if __name__ == '__main__':
    puzzle = []
    with open("data", "r") as data_file:
        for line in data_file:
            puzzle.append(line.rstrip())

    ceres_search = WordPuzzle(puzzle)
    print("Part 1:")
    start = time.time()
    print(f"{ceres_search.get_occurrence_count('XMAS')} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{ceres_search.get_x_mas_occurrence_count()} time: {time.time() - start}s")