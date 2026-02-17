from utils.trie import Trie
from puzzle import Solution

def _preprocess(input_data: str) -> list[str]:
    return input_data.splitlines()

def _part1(lines: list[str]) -> any:
    onsen = Onsen(lines)
    return onsen.get_possible_designs_count()

def _part2(lines: list[str]) -> any:
    onsen = Onsen(lines)
    return onsen.get_all_possible_designs_count()

solution = Solution(
    "Linen Layout",
    "19",
    "2024",
    part1=_part1,
    part2=_part2,
    part1_preprocess=_preprocess,
    part2_preprocess=_preprocess
)

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
        total = 0
        for pattern in self._patterns:
            root = Trie()
            root.add_word(pattern)
            total += self.dfs_is_possible(root)
        return total

    def dfs_is_possible(self, root: Trie) -> int:
        if not root:
            return False
        elif root.word_at_root():
            return True
        else:
            for letter in self._towels_grouped.keys():
                if root.stats_with(letter):
                    for towel in self._towels_grouped[letter]:
                        if self.dfs_is_possible(root.get_branch(towel)):
                            return True
        return False

    def get_all_possible_designs_count(self):
        total = 0
        for pattern in self._patterns:
            root = Trie()
            root.add_word(pattern)
            total += self.dfs_count(root, 0, dict())
        return total

    def dfs_count(self, root: Trie, idx: int, mem: dict) -> int:
        if not root:
            return 0
        elif root.word_at_root():
            return 1
        elif idx in mem:
            return mem[idx]
        else:
            total = 0
            for letter in self._towels_grouped.keys():
                if root.stats_with(letter):
                    for towel in self._towels_grouped[letter]:
                        total += self.dfs_count(root.get_branch(towel), idx + len(towel), mem)
            mem[idx] = total
            return total