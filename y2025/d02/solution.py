import math

from puzzle import Solution
from utils.range import Range


def number_of_digits(n: int) -> int:
    if n < 0:
        # returns number of digits not characters
        # this is very much not needed for this case
        return int(math.log10(-n)) + 1
    elif n == 0:
        return 1
    return int(math.log10(n)) + 1


class ProductRange(Range):
    def __init__(self, start: str, end: str):
        super().__init__(int(start), int(end))
        self.start_str = start
        self.end_str = end

    def get_invalid_ids(self) -> list[int]:
        out = []
        l = len(self.start_str)
        start = self.start
        if l % 2 != 0:
            start = 10 ** l
            l += 1
            if not self.contains_value(start):
                return out
        part_l = l // 2
        mul = (10 ** part_l)
        top_part, bottom_part = start // mul, start % mul
        if bottom_part > top_part:  # example 16 -> 1 - 6 would result in first candidate 11 which is outside the range
            top_part += 1
        while True:
            candidate = top_part * mul + top_part
            if self.contains_value(candidate):
                out.append(candidate)
                top_part += 1
                if top_part >= mul:
                    mul *= 10
            else:
                break
        return out

    def get_all_invalid_ids(self) -> list[int]:
        out = set()
        l_start = len(self.start_str) if self.start > 9 else 2  # no repeats before 9
        l_end = len(self.end_str)
        for l in range(l_start, l_end + 1):
            stop_l = l // 2 + 1
            base = 1
            while True:
                n = number_of_digits(base)
                if n == stop_l:
                    break
                elif l % n != 0:
                    base = 10 ** n
                    continue
                times = l // n
                candidate = 0
                for _ in range(times):
                    candidate *= 10 ** n
                    candidate += base
                if candidate > self.end:
                    base = 10 ** n
                    continue
                elif self.contains_value(candidate):
                    out.add(candidate)
                base += 1
        return list(out)

    @classmethod
    def from_string(cls, entry: str) -> "ProductRange":
        start, end = entry.split("-")
        return cls(start, end)


def _preprocess(data: str) -> list[Range]:
    out = []
    for line in data.split(","):
        out.append(ProductRange.from_string(line))
    return out


def _part1(product_ranges: list[ProductRange]) -> int:
    out = 0
    for product_range in product_ranges:
        out += sum(product_range.get_invalid_ids())
    return out


def _part2(product_ranges: list[ProductRange]) -> int:
    out = 0
    for product_range in product_ranges:
        out += sum(product_range.get_all_invalid_ids())
    return out


solution = Solution("Gift Shop", "2", "2025", part1=_part1, part2=_part2, part1_preprocess=_preprocess,
                    part2_preprocess=_preprocess)
