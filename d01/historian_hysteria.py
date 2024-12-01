from collections import Counter


class HistorianHysteria:
    def __init__(self, list_a: list[int], list_b: list[int]):
        self._list_a = list_a
        self._list_b = list_b

    def get_list_distance(self) -> int:
        return sum([abs(a - b) for a, b in zip(sorted(self._list_a), sorted(self._list_b))])

    def get_list_similarity(self) -> int:
        cnt_list_b = Counter(self._list_b)
        return sum([num * cnt_list_b.get(num, 0) for num in self._list_a])
