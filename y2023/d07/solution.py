import enum
import functools
from typing import Optional

_card_strength = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
    "@": 0
}

class HandStrength(enum.IntEnum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


strength_map = {
    "5": HandStrength.FIVE_OF_A_KIND,
    "41": HandStrength.FOUR_OF_A_KIND,
    "32": HandStrength.FULL_HOUSE,
    "311": HandStrength.THREE_OF_A_KIND,
    "221": HandStrength.TWO_PAIR,
    "2111": HandStrength.ONE_PAIR,
    "11111": HandStrength.HIGH_CARD
}

class CardGame:
    def __init__(self, hands: list[str], is_with_jokers: bool):
        self._hands = []
        for hand in hands:
            cards, bid = hand.split(" ")
            self._hands.append(Hand(cards, int(bid), is_with_jokers))
        self._hands.sort(key=functools.cmp_to_key(Hand.compare))

    def get_winnings(self) -> int:
        sum_bids = 0
        for idx, hand in enumerate(self._hands):
            sum_bids += (idx + 1) * hand.bid
        return sum_bids

class Hand:
   def __init__(self, hand: str, bid: int, is_with_jokers: Optional[bool] = False):
       self.cards = hand
       hand_dict = dict()
       for card in hand:
           hand_dict[card] = hand_dict.get(card, 0) + 1
       jokers = hand_dict["J"] if "J" in hand_dict else 0
       if is_with_jokers and "J" in hand_dict:
           del hand_dict["J"]
           self.cards = self.cards.replace("J", "@")
       cards_sorted = sorted(list(hand_dict.values()), reverse=True)
       if not is_with_jokers:
           pass
       elif cards_sorted:
           cards_sorted[0] += jokers
       else:
           cards_sorted = [jokers]
       self.hand_strength = strength_map["".join(map(str, cards_sorted))]
       self.bid = bid

   @staticmethod
   def compare(hand_a, hand_b) -> int:
       if hand_a.hand_strength > hand_b.hand_strength:
           return 1
       elif hand_a.hand_strength < hand_b.hand_strength:
           return -1
       else:
           for card_a, card_b in zip(hand_a.cards, hand_b.cards):
               if card_a == card_b:
                   pass
               elif _card_strength[card_a] > _card_strength[card_b]:
                   return 1
               else:
                   return -1
           return 0

