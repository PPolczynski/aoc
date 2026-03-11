from puzzle import Solution
from utils.matrix import Matrix


EMPTY = "."
START = "S"
SPLITTER = "^"

MOVE_DOWN = (0, 1)
SPLIT_AND_MOVE_DOWN = [(-1, 1), (1, 1)]

def _preprocess(data: str):
    lines = []
    for i, line in enumerate(data.splitlines()):
        if i == 0 or line.find(SPLITTER) != -1:
            lines.append(line)
    return Matrix(lines, ".")


def _part1(diagram: Matrix) -> int:
    start = diagram.find_first(START)
    beams = {start}
    splits = 0
    while len(beams) > 0:
        tmp = set()
        for beam in beams:
            if diagram.is_out_of_bounds(beam):
                continue
            if diagram[beam] == SPLITTER:
                splits += 1
                for dx, dy in SPLIT_AND_MOVE_DOWN:
                    tmp.add((beam[0] + dx, beam[1] + dy))
            else:
                tmp.add((beam[0] + MOVE_DOWN[0], beam[1] + MOVE_DOWN[1]))
        beams = tmp
    return splits

def _part2(diagram: Matrix) -> int:
    mem = dict()
    start = diagram.find_first(START)

    def dfs(beam: tuple[int,int]) -> int:
        if diagram.is_out_of_bounds(beam):
            return 0
        elif beam in mem:
            return mem[beam]
        if diagram[beam] == SPLITTER:
            timelines = 1
            for dx, dy in SPLIT_AND_MOVE_DOWN:
                timelines += dfs((beam[0] + dx, beam[1] + dy))
            mem[beam] = timelines
        else:
            mem[beam] = dfs((beam[0] + MOVE_DOWN[0], beam[1] + MOVE_DOWN[1]))
        return mem[beam]
    return 1 + dfs(start)

solution = Solution("Laboratories", "7", "2025",
                    part1=_part1,
                    part2=_part2,
                    part1_preprocess=_preprocess,
                    part2_preprocess=_preprocess)
