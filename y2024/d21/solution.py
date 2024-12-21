import re
from collections import deque, defaultdict

_keypad_numeric = "NUMERIC"
_keypad_directional = "DIRECTIONAL"

_keypad = {
    "NUMERIC" : {
        "A": {
            "0": "<",
            "3": "^"
        },
        "0": {
            "A": ">",
            "2": "^"
        },
        "3": {
            "A": "v",
            "2": "<",
            "6": "^"
        },
        "2": {
            "0": "v",
            "1": "<",
            "5": "^",
            "3": ">"
        },
        "1": {
            "4": "^",
            "2": ">"
        },
        "6": {
            "5": "<",
            "9": "^",
            "3": "v"
        },
        "5": {
            "4": "<",
            "8": "^",
            "6": ">",
            "2": "v"
        },
        "4": {
            "7": "^",
            "5": ">",
            "1": "v"
        },
        "9": {
            "8": "<",
            "6": "v"
        },
        "8": {
            "7": "<",
            "9": ">",
            "5": "v"
        },
        "7": {
            "8": ">",
            "4": "v"
        }
    },
    "DIRECTIONAL" :  {
        "A": {
            "^": "<",
            ">": "v"
        },
        "^": {
            "A": ">",
            "v": "v"
        },
        ">": {
            "A": "^",
            "v": "<"
        },
        "v": {
            "^": "^",
            ">": ">",
            "<": "<"
        },
        "<": {
            "v": ">"
        }
    }
}

_start = "A"
_press_button = _start

class Keypads:
    def __init__(self):
        self._paths_mem = defaultdict(dict)
        self._moves_mem = defaultdict(dict)

    def _get_shortest_path(self, _keypad_key, _from, _to) -> list[str]:
        if _keypad_key in self._paths_mem and (_from, _to) in self._paths_mem[_keypad_key]:
            return self._paths_mem[_keypad_key][(_from, _to)]
        graph = _keypad[_keypad_key]
        queue = deque([(_from, [])])
        visited = dict()
        shortest = float("Inf")
        paths = []
        while queue:
            key, path = queue.popleft()
            if key == _to:
                path.append(_press_button)
                length = len(path)
                if length == shortest:
                    paths.append("".join(path))
                elif length < shortest:
                    paths = ["".join(path)]
                    shortest = length
                continue
            elif key in visited and len(path) > visited[key]:
                continue
            node = graph[key]
            visited[key] = len(path)
            for neighbour in node.keys():
                n_path = path.copy()
                n_path.append(node[neighbour])
                queue.append((neighbour, n_path))
        self._paths_mem[_keypad_key][(_from, _to)] = paths
        return paths

    def get_moves(self, keyboard_type: str, sequence : str) :
        current = _start
        out = []
        for character in sequence:
            out.append(self._get_shortest_path(keyboard_type, current, character))
            current = character
        return out

    def _dfs(self, sequence, remaining):
        if not remaining:
            return len(sequence)
        elif sequence in self._moves_mem and remaining in self._moves_mem[sequence]:
            return self._moves_mem[sequence][remaining]
        else:
            total = 0
            moves = self.get_moves(_keypad_directional, sequence)
            for options in moves:
                total += min([self._dfs(option, remaining - 1) for option in options])
            self._moves_mem[sequence][remaining] = total
            return total

    def _get_sequence_length(self, code: str, number_of_robots: int) -> int:
        sequences = self.get_moves(_keypad_numeric, code)
        total = 0
        for options in sequences:
            total += min([self._dfs(option, number_of_robots) for option in options])
        return total

    def get_codes_complexity(self, codes: list[str], number_of_robots: int) -> int:
        total = 0
        for code in codes:
            digit = int(re.findall("\d+", code)[0])
            length = self._get_sequence_length(code, number_of_robots)
            total += digit * length
        return total