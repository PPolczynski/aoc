import unittest

from y2023.d07.camel_cards import Hand, HandStrength, CamelCards


class CamelCardsTestCase(unittest.TestCase):
    def test_hand(self):
        hand1 = Hand("32T3K", 765)
        self.assertEqual(HandStrength.ONE_PAIR, hand1.hand_strength)
        hand2 = Hand("KK677", 684)
        self.assertEqual(HandStrength.TWO_PAIR, hand2.hand_strength)
        hand3 = Hand("T55J5", 28)
        self.assertEqual(HandStrength.THREE_OF_A_KIND, hand3.hand_strength)
        hand4 = Hand("22233", 1)
        self.assertEqual(HandStrength.FULL_HOUSE, hand4.hand_strength)
        hand5 = Hand("23456", 1)
        self.assertEqual(HandStrength.HIGH_CARD, hand5.hand_strength)
        hand6 = Hand("22222", 1)
        self.assertEqual(HandStrength.FIVE_OF_A_KIND, hand6.hand_strength)
        hand6 = Hand("22223", 1)
        self.assertEqual(HandStrength.FOUR_OF_A_KIND, hand6.hand_strength)

    def test_hand_compare(self):
        hand1 = Hand("KK677", 1)
        hand2 = Hand("KTJJT", 1)
        self.assertEqual(1, Hand.compare(hand1, hand2))
        hand3 = Hand("QQQJA", 1)
        hand4 = Hand("T55J5", 1)
        self.assertEqual(-1, Hand.compare(hand4, hand3))
        hand5 = Hand("22222", 1)
        hand6 = Hand("22222", 1)
        self.assertEqual(0, Hand.compare(hand5, hand6))

    def test_get_winnings(self):
        hands = [
            "32T3K 765",
            "T55J5 684",
            "KK677 28",
            "KTJJT 220",
            "QQQJA 483"
        ]
        camel_cards = CamelCards(hands)
        self.assertEqual(6440, camel_cards.get_winnings())

if __name__ == '__main__':
    unittest.main()
