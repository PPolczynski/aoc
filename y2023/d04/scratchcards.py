import re
from collections import deque


class Scratchcards:

    @staticmethod
    def get_scratchcards_score(scratchcards: list[str]) -> int:
        score = 0
        for scratchcard in scratchcards:
            _, card_numbers, wining_numbers = Scratchcards._get_lists_from_scratchcard(scratchcard)
            winning_cnt = len(set(card_numbers).intersection(set(wining_numbers)))
            if winning_cnt > 0:
                score += pow(2, winning_cnt - 1)
        return score

    @staticmethod
    def get_scratchcards_count(scratchcards: list[str]):
        last_scratch_card_id = len(scratchcards) #ids are 1 based
        pre_processed_cards = dict()
        for scratchcard in scratchcards:
            card_id, card_numbers, wining_numbers = Scratchcards._get_lists_from_scratchcard(scratchcard)
            winning_cnt = len(set(card_numbers).intersection(set(wining_numbers)))
            pre_processed_cards[card_id] = winning_cnt
        cards = {}
        for card_id in range(1, last_scratch_card_id + 1):
            if card_id not in cards:
                cards[card_id] = 1
            score = pre_processed_cards[card_id]
            offset = 0
            while offset < score and (card_id + 1) < last_scratch_card_id:
                offset += 1
                cards[card_id + offset] = cards.get(card_id + offset, 1) + cards[card_id]
        return sum(cards.values())

    @staticmethod
    def _get_lists_from_scratchcard(scratchcard: str) -> tuple[int, list[int], list[int]]:
        card_parts = scratchcard.split(": ")
        card_id = int(re.findall("\d+", card_parts[0])[0])
        card_numbers, wining_numbers = card_parts[1].split(" | ")
        def _numbers_str_to_list(numbers: str) -> list[int]:
            return [int(num) for num in re.findall("\d+", numbers)]
        return card_id, _numbers_str_to_list(card_numbers), _numbers_str_to_list(wining_numbers)

