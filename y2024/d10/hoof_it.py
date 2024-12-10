from utils.matrix import Matrix

_empty_space = "."
_start = "0"
_end = "9"
_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class HoofIt:

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
