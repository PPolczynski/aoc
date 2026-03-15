import re

from puzzle import Solution
from utils.polygon import Polygon
from utils.range import Range


def _preprocess(data: str) -> list[tuple[int, int]]:
    pattern = r"\d+"
    return [(int(x), int(y)) for x, y in [re.findall(pattern, line) for line in data.splitlines()]]


def area(a: tuple[int, int], b: tuple[int, int]) -> float:
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)


def _part1(points: list[tuple[int, int]]) -> int:
    max_area = -1
    for idx, point in enumerate(points):
        for other_point in points[idx + 1:]:
            max_area = max(area(point, other_point), max_area)
    return max_area


def _part2(points: list[tuple[int, int]]) -> int:
    x_values, y_values = sorted(set([x for x, _ in points])), sorted(set([y for _, y in points]))
    x_map = {x: i for i, x in enumerate(x_values)}
    y_map = {y: i for i, y in enumerate(y_values)}
    compressed = [(x_map[x], y_map[y]) for x, y in points]
    polygon_as_row_ranges = Polygon(compressed).as_ranges()
    max_area = -1
    for idx, (x1, y1) in enumerate(compressed):
        other_idx = idx
        for x2, y2 in compressed[idx + 1:]:
            other_idx += 1
            current_area = area(points[idx], points[other_idx])
            if current_area > max_area:
                rectangle = Range(start=min(x1, x2), end=max(x1, x2))
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    if y not in polygon_as_row_ranges:
                        break
                    inside_ranges = polygon_as_row_ranges[y]
                    if not any(inside_range.contains(rectangle) for inside_range in inside_ranges):
                        break
                else:
                    max_area = current_area

    return max_area


solution = Solution("Movie Theater", "9", "2025",
                    part1=_part1,
                    part2=_part2,
                    part1_preprocess=_preprocess,
                    part2_preprocess=_preprocess)
