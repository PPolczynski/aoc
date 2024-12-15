import re
import time

from y2023.d07.camel_cards import CamelCards

if __name__ == '__main__':
    lines = []
    with open("data", "r") as data_file:
        for line in data_file:
            lines.append(line.rstrip())
    camel_cards = CamelCards(lines, False)
    print("Part 1:")
    start = time.time()
    print(f"{camel_cards.get_winnings()} time: {time.time() - start}s")

    camel_cards_jokers = CamelCards(lines, True)
    print("Part2:")
    start = time.time()
    print(f"{camel_cards_jokers.get_winnings()} time: {time.time() - start}s")