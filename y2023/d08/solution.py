import math
import re
from puzzle import Solution

_directions = {
    "L" : 0,
    "R" : 1
}
_start = "AAA"
_target = "ZZZ"
_ghost_start = "A"
_ghost_end = "Z"

def _preprocess(input_data: str) -> tuple[str, list[str]]:
    lines = input_data.splitlines()
    moves, _, *graph = lines
    return moves, graph

def _part1(data: tuple[str, list[str]]) -> any:
    moves, graph = data
    island_map = IslandMap(graph)
    return island_map.get_steps_count(moves)

def _part2(data: tuple[str, list[str]]) -> any:
    moves, graph = data
    island_map = IslandMap(graph)
    return island_map.get_steps_count_ghost(moves)

solution = Solution(
    "Haunted Wasteland",
    "8",
    "2023",
    part1=_part1,
    part2=_part2,
    part1_preprocess=_preprocess,
    part2_preprocess=_preprocess
)

class IslandMap:
    def __init__(self, lines: list[str]):
        graph = dict()
        ghost_start = []
        for line in lines:
            value, left, right = re.findall("\w+", line)
            graph[value] = (left, right, value.endswith(_ghost_end))
            if value.endswith(_ghost_start):
                ghost_start.append(value)
        self._graph = graph
        self._ghost_start = ghost_start

    @staticmethod
    def _get_move(moves: str, idx: int) -> tuple[int, int]:
        if idx >= len(moves):
            idx = 0
        move = _directions[moves[idx]]
        idx += 1
        return move, idx

    def get_steps_count(self, moves: str) -> int:
        steps = 0
        i = 0
        current = self._graph[_start]
        while True:
            steps += 1
            move, i = self._get_move(moves, i)
            label = current[move]
            if label == _target:
                break
            else:
                current = self._graph[label]
        return steps

    def get_steps_count_ghost(self, moves: str) -> int:
        steps_until_z = dict()
        steps = 0
        i = 0
        positions = self._ghost_start
        while True:
            steps += 1
            new_positions = []
            move, i = self._get_move(moves, i)
            for idx, label in enumerate(positions):
                nxt = self._graph[label][move]
                new_positions.append(nxt)
                if self._graph[nxt][2]:
                    steps_until_z[idx] = steps
            if len(steps_until_z) == len(positions):
                break
            else:
                positions = new_positions
        return math.lcm(*steps_until_z.values())
