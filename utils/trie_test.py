import unittest

from .trie import Trie


class TrieTestCase(unittest.TestCase):
    def test_adding_getting(self):
        trie = Trie()
        trie.add_word("orange")
        trie.add_word("apple")
        trie.add_word("banana")
        words = trie.get_words()
        self.assertEqual(len(words), 3)
        self.assertIn("orange", words)
        self.assertIn("apple", words)
        self.assertIn("banana", words)

    def test_has_word(self):
        trie = Trie()
        trie.add_word("orange")
        trie.add_word("apple")
        trie.add_word("banana")
        words = trie.get_words()
        self.assertEqual(len(words), 3)
        self.assertTrue(trie.has_word("orange"))
        self.assertTrue(trie.has_word("apple"))
        self.assertTrue(trie.has_word("banana"))
        self.assertTrue(trie.has_word("Orange"))
        self.assertTrue(trie.has_word("ORANGE"))
        self.assertFalse(trie.has_word("lemon"))

    def test_starts_with(self):
        trie = Trie()
        trie.add_word("mobile")
        trie.add_word("mouse")
        trie.add_word("moneypot")
        trie.add_word("monitor")
        trie.add_word("mousepad")
        self.assertEqual(len(trie.get_words()), 5)
        print(trie.stats_with("mo"))
        self.assertEqual(len(trie.stats_with("mo")), 5)
        print(trie.stats_with("mou"))
        self.assertEqual(len(trie.stats_with("mou")), 2)
        print(trie.stats_with("mon"))
        self.assertEqual(len(trie.stats_with("mon")), 2)
        print(trie.stats_with("ma"))
        self.assertEqual(len(trie.stats_with("ma")), 0)
        print(trie.stats_with("mobile"))
        self.assertEqual(len(trie.stats_with("mobile")), 1)

if __name__ == '__main__':
    unittest.main()
