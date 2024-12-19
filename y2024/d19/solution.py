from multiprocessing import Pool

from utils.trie import Trie


class Onsen:
    def __init__(self, patterns_and_towels: list[str]):
        towels , _, *patterns  = patterns_and_towels
        self._towels = towels.split(", ")
        self._towels_grouped = dict()
        for towel in self._towels:
            if towel[0] not in self._towels_grouped:
                self._towels_grouped[towel[0]] = [towel]
            else:
                self._towels_grouped[towel[0]].append(towel)
        self._patterns = patterns

    def get_possible_designs_count(self) -> int:
        possible_patterns = set()
        for pattern in self._patterns:
            t = Trie()
            t.add_word(pattern)
            candidates = [t]
            while candidates:
                candidate = candidates.pop()
                if not candidate:
                    continue
                elif candidate.word_at_root():
                    possible_patterns.add(candidate.word_at_root())
                    break
                for letter in self._towels_grouped.keys() :
                    if candidate.stats_with(letter):
                        for towel in self._towels_grouped[letter]:
                            node = candidate.get_branch(towel)
                            if node:
                                candidates.append(node)
        return len(possible_patterns)