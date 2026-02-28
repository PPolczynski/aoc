import re
from dataclasses import dataclass

from puzzle import Solution
from utils.range import Range


@dataclass
class HailStone:
    x: int
    y: int
    z: int
    vx: int
    vy: int
    vz: int

    def intersects_xy(self, other: "HailStone") -> tuple[bool, tuple[float, float] | None]:
        d_x, d_y = self.x - other.x, self.y - other.y
        denominator = self.vy * other.vx - self.vx * other.vy
        if denominator == 0:
            return False, None
        t_x = (other.vy * d_x - other.vx * d_y) / denominator
        if t_x <= 0:
            return False, None
        t_y = (self.vy * d_x - self.vx * d_y) / denominator
        if t_y <= 0:
            return False, None
        return True, (self.x + t_x * self.vx, self.y + t_x * self.vy)

    @classmethod
    def from_line(cls, line: str) -> "HailStone":
        x, y, z, vx, vy, vz = re.findall(r"-?\d+", line)
        return cls(int(x), int(y), int(z), int(vx), int(vy), int(vz))


def _part1(stones: list[HailStone]) -> int:
    x_range, y_range = Range(200000000000000, 400000000000000), Range(200000000000000, 400000000000000)
    cnt = 0
    for idx, s1 in enumerate(stones[:-1]):
        for s2 in stones[idx + 1:]:
            intersects, coord = s1.intersects_xy(s2)
            if intersects and x_range.start <= coord[0] <= x_range.end and y_range.start <= coord[1] <= y_range.end:
                cnt += 1
    return cnt


def _part2(stones: list[HailStone]) -> int:
    return 0


def _preprocess(data) -> list[HailStone]:
    return [HailStone.from_line(line) for line in data.splitlines()]


solution = Solution("Never Tell Me The Odds", "24", "2023", part1=_part1, part2=_part2, part1_preprocess=_preprocess,
                    part2_preprocess=_preprocess)
