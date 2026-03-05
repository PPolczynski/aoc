from puzzle import Solution
from utils.range import Range


class ProductRange(Range):
    def __init__(self, start: str, end: str):
        super().__init__(int(start), int(end))
        self.start_str = start

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


def _part2(rotations: list[ProductRange]) -> int:
    pass


solution = Solution("Gift Shop", "2", "2025", part1=_part1, part2=_part2, part1_preprocess=_preprocess,
                    part2_preprocess=_preprocess)
