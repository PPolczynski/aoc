from utils.matrix import Matrix
from puzzle import Solution

_empty_space = "."
_start = "0"
_end = "9"
_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def _preprocess(input_data: str) -> list[str]:
    return input_data.splitlines()

def _part1(topo: list[str]) -> any:
    hiking_guide = HikingGuide(topo)
    return hiking_guide.get_trailheads_score_sum()

def _part2(topo: list[str]) -> any:
    hiking_guide = HikingGuide(topo)
    return hiking_guide.get_trailheads_score_distinct_paths_sum()

solution = Solution(
    "Hoof It",
    "10",
    "2024",
    part1=_part1,
    part2=_part2,
    part1_preprocess=_preprocess,
    part2_preprocess=_preprocess
)

class HikingGuide:
    def __init__(self, topographic_map: list[str]):
        self._topo = Matrix(topographic_map)

    def get_trailheads_score_sum(self) -> int:
        total = 0
        for start in self._get_starts():
            ends = self._dfs(start, -1, dict())
            total += len(ends)
        return total

    def _get_starts(self) -> list[tuple[int, int]]:
        starts = []
        for value, coordinates in self._topo:
            if value == _start:
                starts.append(coordinates)
        return starts

    def get_trailheads_score_distinct_paths_sum(self) -> int:
        total = 0
        for start in self._get_starts():
            total += self._dfs_paths(start, -1, dict())
        return total

    def _dfs(self, coordinate: tuple[int, int], previous_level: int, mem: dict) -> set:
        if self._topo.is_out_of_bounds(coordinate) or self._topo[coordinate] == _empty_space:
            return set()
        elif int(self._topo[coordinate]) - previous_level != 1:
            return set()
        elif self._topo[coordinate] == _end:
            return {coordinate}
        else:
            if coordinate not in mem:
                x, y = coordinate
                reachable_ends = set()
                for dx, dy in _directions:
                    reachable_ends |= self._dfs((x + dx, y + dy), int(self._topo[coordinate]), mem)
                mem[coordinate] = reachable_ends
            return mem[coordinate]

    def _dfs_paths(self, coordinate: tuple[int, int], previous_level: int, mem: dict) -> int:
        if self._topo.is_out_of_bounds(coordinate) or self._topo[coordinate] == _empty_space:
            return 0
        elif int(self._topo[coordinate]) - previous_level != 1:
            return 0
        elif self._topo[coordinate] == _end:
            return 1
        else:
            if coordinate not in mem:
                x, y = coordinate
                paths = 0
                for dx, dy in _directions:
                    paths += self._dfs_paths((x + dx, y + dy), int(self._topo[coordinate]), mem)
                mem[coordinate] = paths
            return mem[coordinate]