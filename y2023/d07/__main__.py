import re
import time

from y2023.d07.solution import CardGame

if __name__ == '__main__':
    lines = []
    with open("data", "r") as data_file:
        for line in data_file:
            lines.append(line.rstrip())
    card_game = CardGame(lines, False)
    print("Part 1:")
    start = time.time()
    print(f"{card_game.get_winnings()} time: {time.time() - start}s")

    camel_cards_jokers = CardGame(lines, True)
    print("Part2:")
    start = time.time()
    print(f"{camel_cards_jokers.get_winnings()} time: {time.time() - start}s")