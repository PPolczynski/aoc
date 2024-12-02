_EOW = "##EOW##"

class Trie:
    def __init__(self):
        self._root = dict()

    def add_word(self, word: str) -> None:
        if word:
            self._add_word(word.lower(), word.lower())

    def _add_word(self, word_part: str, word: str) -> None:
        if not word_part:
            self._root[_EOW] = word
            return
        first_character = word_part[0]
        if first_character not in self._root:
            self._root[first_character] = Trie()
        # noinspection PyProtectedMember
        self._root[first_character]._add_word(word_part[1:], word)


    def get_words(self):
        out = []
        for key, value in self._root.items():
            if key == _EOW:
                out.append(value)
            else:
                out += value.get_words()
        return out

    def has_word(self, word: str) -> bool:
        if not word and _EOW in self._root:
            return True
        elif not word:
            return False
        first_char = word[0].lower()
        if first_char in self._root:
            return self._root[first_char].has_word(word[1:])
        else:
            return False

    def stats_with(self, prefix:str) -> list[str]:
        if not prefix:
            return self.get_words()
        else:
            first_char = prefix[0].lower()
            if first_char in self._root:
                return self._root[first_char].stats_with(prefix[1:])
            else:
                return []
