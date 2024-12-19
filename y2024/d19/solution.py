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
            root = Trie()
            root.add_word(pattern)
            candidates = [root]
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

    def get_all_possible_designs_count(self):
        total = 0
        for pattern in self._patterns:
            root = Trie()
            root.add_word(pattern)
            total += self.dfs(root, 0, dict())
        return total

    def dfs(self, root: Trie, idx: int, mem: dict) -> int:
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
                        total += self.dfs(root.get_branch(towel), idx + len(towel), mem)
            mem[idx] = total
            return total