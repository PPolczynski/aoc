import enum
import functools

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
    "2": 1
}

class HandStrength(enum.IntEnum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


class CamelCards:
    def __init__(self, hands: list[str]):
        self._hands = []
        for hand in hands:
            cards, bid = hand.split(" ")
            self._hands.append(Hand(cards, int(bid)))
        self._hands.sort(key=functools.cmp_to_key(Hand.compare))

    def get_winnings(self):
        sum_bids = 0
        for idx, hand in enumerate(self._hands):
            sum_bids += (idx + 1) * hand.bid
        return sum_bids

class Hand:
   def __init__(self, hand: str, bid: int):
       self.cards = hand
       hand_dict = dict()
       for card in hand:
           hand_dict[card] = hand_dict.get(card, 0) + 1
       strength_map = {
           "5": HandStrength.FIVE_OF_A_KIND,
           "41": HandStrength.FOUR_OF_A_KIND,
           "32" : HandStrength.FULL_HOUSE,
           "311" : HandStrength.THREE_OF_A_KIND,
           "221" : HandStrength.TWO_PAIR,
           "2111" : HandStrength.ONE_PAIR,
           "11111" : HandStrength.HIGH_CARD
       }
       self.hand_strength = strength_map["".join(map(str, sorted(list(hand_dict.values()), reverse=True)))]
       self.bid = bid

   def __str__(self):
       return f"{self.cards} strength: {self.hand_strength}"

   def __repr__(self):
       return f"{self.cards} strength: {self.hand_strength}"

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

