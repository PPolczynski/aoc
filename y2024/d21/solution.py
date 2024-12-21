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

mem = defaultdict(dict)
mem2 = defaultdict(dict)

def get_shortest_path(_keypad_key, _from, _to) -> list[str]:
    if _keypad_key in mem and (_from, _to) in mem[_keypad_key]:
        return mem[_keypad_key][(_from, _to)]
    graph = _keypad[_keypad_key]
    queue = deque([(_from, [])])
    visited = dict()
    shortest = float("Inf")
    paths = []
    while queue:
        key, path = queue.popleft()
        if key == _to:
            path.append("A")
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
    mem[_keypad_key][(_from, _to)] = paths
    return paths

def get_moves_numerical(code : str) :
    current = "A"
    out = []
    for character in code:
        out.append(get_shortest_path(_keypad_numeric, current, character))
        current = character
    return out

def get_moves_directional(keys : str) -> list[str] :
    current = "A"
    out = []
    for key in keys:
        out.append(get_shortest_path(_keypad_directional, current, key))
        current = key
    return out

def dfs(sequence, remaining, memmem):
    if not remaining:
        return len(sequence)
    elif sequence in memmem and remaining in memmem[sequence]:
        return memmem[sequence][remaining]
    else:
        total = 0
        moves = get_moves_directional(sequence)
        for options in moves:
            total += min([dfs(option, remaining - 1, memmem) for option in options])
        memmem[sequence][remaining] = total
        return total

def get_sequence_length(code: str, number_of_robots: int):
    sequences = get_moves_numerical(code)
    total = 0
    for options in sequences:
        total += min([dfs(option, number_of_robots, mem2) for option in options])
    return total

def get_codes_complexity(codes: list[str], number_of_robots: int):
    total = 0
    for code in codes:
        digit = int(re.findall("\d+", code)[0])
        length = get_sequence_length(code, number_of_robots)
        total += digit * length
    return total