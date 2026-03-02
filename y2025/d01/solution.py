from dataclasses import dataclass

from puzzle import Solution

_direction_to_int = {"L": -1, "R": 1}

_range_end = 99
_range_start = 0
_start_position = 50
_target = 0


@dataclass
class Rotation:
    direction: int
    clicks: int
    full_rotations: int

    @classmethod
    def from_line(cls, line: str) -> 'Rotation':
        direction, clicks, full_rotations = _direction_to_int[line[:1]], int(line[1:]), 0
        if clicks > _range_end:
            full_rotations = clicks // _range_end
            clicks %= _range_end
            clicks -= full_rotations  # because of extra click between 99 and 0
        if clicks < 0:
            full_rotations -= 1 # extra clicks between 99 0 has division to be one extra
            clicks += _range_end + 1  # +1 because 99 to 0 is extra click that was not taken
        return Rotation(direction, clicks, full_rotations)

    def rotate_from(self, position: int) -> tuple[int, bool]:
        next_position = position + self.direction * self.clicks
        passed = False
        if next_position > _range_end:
            next_position = next_position - _range_end - 1
            passed = True
        elif next_position < _range_start:
            next_position = _range_end + next_position + 1
            passed = True
        return next_position, passed

    def rotate_from_with_pass_cnt(self, position: int) -> [int, int]:
        starts_at_target = position == _target
        passes_from_clicks = 0
        next_position, passed = self.rotate_from(position)
        if next_position == _target and self.clicks != 0:
            passes_from_clicks = 1
        elif passed and not starts_at_target:
            passes_from_clicks = 1
        return next_position, self.full_rotations + passes_from_clicks

def _preprocess(data: str) -> list[Rotation]:
    return [Rotation.from_line(line) for line in data.splitlines()]


def _part1(rotations: list[Rotation]) -> int:
    position = _start_position
    cnt = 0
    for rotation in rotations:
        position, _ = rotation.rotate_from(position)
        if position == _target:
            cnt += 1
    return cnt


def _part2(rotations: list[Rotation]) -> any:
    position = _start_position
    cnt = 0
    for rotation in rotations:
        position, passes = rotation.rotate_from_with_pass_cnt(position)
        cnt += passes
    return cnt


solution = Solution("Secret Entrance", "1", "2025", part1=_part1, part2=_part2, part1_preprocess=_preprocess,
                    part2_preprocess=_preprocess)
