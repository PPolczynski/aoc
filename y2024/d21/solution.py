import itertools
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

def get_combinations(moves):
    out = [""]
    for paths in moves:
        tmp = []
        for path in paths:
            for o in out:
                tmp.append(o + path)
        out = tmp
    return out

def get_moves_numerical(code : str) :
    current = "A"
    out = []
    for letter in code:
        out.append(get_shortest_path(_keypad_numeric, current, letter))
        out.append("A")
        current = letter
    return get_combinations(out)

def get_moves_directional(code : str) -> list[str] :
    current = "A"
    out = []
    for letter in code:
        out.append(get_shortest_path(_keypad_directional, current, letter))
        out.append("A")
        current = letter
    return get_combinations(out)

def get_directional_moves(moves):
    directional_moves = []
    for path in moves:
        directional_moves += get_moves_directional(path)
    shortest = min([len(moves) for moves in directional_moves])
    return list(filter(lambda m:len(m) == shortest, directional_moves))

def get_moves(code):
    robots = 2
    moves = get_moves_numerical(code)
    for r in range(0, robots):
        moves = get_directional_moves(moves)
    return moves

def get_codes_complexity(codes: list[str]):
    total = 0
    for code in codes:
        digit = int(re.findall("\d+", code)[0])
        length = len(get_moves(code)[0])
        total += digit * length
    return total