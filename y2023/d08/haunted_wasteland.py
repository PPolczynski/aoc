import re

_directions = {
    "L" : 0,
    "R" : 1
}
_start = "AAA"
_target = "ZZZ"

class HauntedWasteland:
    def __init__(self, lines: list[str]):
        graph = dict()
        for line in lines:
            value, left, right = re.findall("\w+", line)
            graph[value] = (left, right)
        self._graph = graph

    def get_steps_count(self, moves: str) -> int:
        steps = 0
        i = 0
        current = self._graph[_start]
        while True:
            steps += 1
            if i >= len(moves):
                i = 0
            label = current[_directions[moves[i]]]
            if label == _target:
                break
            else:
                current = self._graph[label]
                i += 1
        return steps
