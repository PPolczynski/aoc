from puzzle import Solution
from utils.range import Range


def _preprocess(data: str) -> tuple[list[Range], list[int]]:
    ranges_str, ids_str = data.split("\n\n")
    ranges = []
    for range_str in ranges_str.splitlines():
        start, end = range_str.split("-")
        ranges.append(Range(int(start), int(end)))
    ids = [int(num) for num in ids_str.splitlines()]
    return ranges, ids


def _part1(data: tuple[list[Range], list[int]]) -> int:
    ranges, ids = data
    cnt = 0
    ranges = Range.simplify_ranges(ranges)
    for i in ids:
        for r in ranges:
            if r.contains_value(i):
                cnt += 1
                break
    return cnt


def _part2(data: tuple[list[Range], list[int]]) -> int:
    ranges, _ = data
    return sum(len(r) for r in Range.simplify_ranges(ranges))


solution = Solution("Cafeteria", "5", "2025",
                    part1=_part1,
                    part2=_part2,
                    part1_preprocess=_preprocess,
                    part2_preprocess=_preprocess)
