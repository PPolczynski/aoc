from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class Range:
    start: int
    end: int

    def __post_init__(self):
        if self.start > self.end:
            raise ValueError(f"Range start ({self.start}) cannot be greater than end ({self.end})")

    def contains(self, other: 'Range') -> bool:
        return self.start <= other.start and self.end >= other.end

    def is_contained_by(self, other: 'Range') -> bool:
        return other.contains(self)

    def overlaps(self, other: 'Range') -> bool:
        return max(self.start, other.start) <= min(self.end, other.end)

    def contains_value(self, value: int) -> bool:
        return self.start <= value <= self.end

    def __len__(self) -> int:
        return self.end - self.start + 1

    def merge(self, other: 'Range') -> 'Range':
        if not self.overlaps(other):
            raise ValueError(f"Cannot merge disjoint ranges: {self} and {other}")
        return Range(min(self.start, other.start), max(self.end, other.end))

    def __lt__(self, other: 'Range') -> bool:
        if not isinstance(other, Range):
            return NotImplemented
        return (self.start, self.end) < (other.start, other.end)


def simplify_ranges(ranges: List[Range]) -> List[Range]:
    if not ranges:
        return []
    
    sorted_ranges = sorted(ranges)
    simplified = [sorted_ranges[0]]
    
    for current in sorted_ranges[1:]:
        last = simplified[-1]
        if last.overlaps(current):
            simplified[-1] = last.merge(current)
        else:
            simplified.append(current)
            
    return simplified
