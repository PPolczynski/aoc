import time

from y2023.d04.scratchcards import Scratchcards

if __name__ == '__main__':
    scratchcards = []
    with open("data", "r") as data_file:
        for line in data_file:
            scratchcards.append(line.rstrip())
    print("Part 1:")
    start = time.time()
    print(f"{Scratchcards.get_scratchcards_score(scratchcards)} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{Scratchcards.get_scratchcards_count(scratchcards)} time: {time.time() - start}s")