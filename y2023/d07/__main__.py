import re
import time

from y2023.d07.camel_cards import CamelCards

if __name__ == '__main__':
    lines = []
    with open("data", "r") as data_file:
        for line in data_file:
            lines.append(line.rstrip())
    camel_cards = CamelCards(lines)
    print("What are the total winnings?")
    start = time.time()
    print(f"{camel_cards.get_winnings()} time: {time.time() - start}s")

    # races = [(int("".join(lines[0])), int("".join(lines[1])))]
    # print("How many ways can you beat the record in this one much longer race?")
    # start = time.time()
    # print(f"{WaitForIt.get_product_ways_to_beat_time(races)} time: {time.time() - start}s")