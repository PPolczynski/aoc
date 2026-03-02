from dataclasses import dataclass

from puzzle import Solution

_direction_to_int = {"L": -1, "R": 1}

_range_end = 99
_range_start = 0
_start_position = 50


@dataclass
class Rotation:
    direction: int
    clicks: int

    @classmethod
    def from_line(cls, line: str) -> 'Rotation':
        direction, clicks = _direction_to_int[line[:1]], int(line[1:])
        if clicks > _range_end:
            times = clicks // _range_end
            clicks %= _range_end
            clicks -= times  # because of extra click between 99 and 0
        if clicks < 0:
            clicks += _range_end + 1  # +1 because 99 to 0 is extra click that was not taken
        return Rotation(direction, clicks)

    def position_after(self, position: int) -> int:
        next_position = position + self.direction * self.clicks
        if next_position > _range_end:
            next_position = next_position - _range_end - 1
        elif next_position < _range_start:
            next_position = _range_end + next_position + 1
        return next_position


def _preprocess(data: str) -> list[Rotation]:
    return [Rotation.from_line(line) for line in data.splitlines()]


def _part1(rotations: list[Rotation]) -> int:
    position = _start_position
    cnt = 0
    for rotation in rotations:
        position = rotation.position_after(position)
        if position == 0:
            cnt += 1
    return cnt


def _part2(rotations: list[Rotation]) -> any:
    pass


solution = Solution("Secret Entrance", "1", "2025", part1=_part1, part2=_part2, part1_preprocess=_preprocess,
                    part2_preprocess=_preprocess)
