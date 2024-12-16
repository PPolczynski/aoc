from collections import deque

from utils.matrix import Matrix

_wall = "#"
_box = "O"
_robot = "@"
_empty = "."
_box_left = "["
_box_right = "]"

_moves = {
    "^" : (0, -1),
    ">" : (1, 0),
    "v" : (0, 1),
    "<" : (-1, 0)
}

_wider = {
    "." : "..",
    "@" : "@.",
    "O" : "[]",
    "#" : "##"
}

class Warehouse:
    def __init__(self, warehouse: list[str],  is_wide: bool = False):
        wide_warehouse = []
        if is_wide:
            for row in warehouse:
                wide_warehouse.append("".join([_wider[char] for char in row]))
        self._warehouse = Matrix(warehouse if not is_wide else wide_warehouse, _wall)
        self._is_wide = is_wide

    def apply_moves(self, move_groups: list[str]) -> None:
        robot_position = self._warehouse.find(_robot)[0]
        for moves in move_groups:
            for move in moves:
                robot_position = self._move(robot_position, _moves[move]) \
                    if not self._is_wide else self._move_wide(robot_position, _moves[move])


    def _move(self, position: tuple[int, int], move: tuple[int, int]) -> tuple[int, int]:
        x, y = position
        dx, dy = move
        n_x, n_y = x + dx, y + dy
        symbol = self._warehouse[(x, y)]
        if self._warehouse[(n_x, n_y)] == _empty:
            self._warehouse[(n_x, n_y)] = symbol
            self._warehouse[(x, y)] = _empty
            return n_x, n_y
        elif self._warehouse[(n_x, n_y)] == _wall:
            return x, y
        else:
            result = self._move((n_x, n_y), move)
            if result == (n_x, n_y):
                return x, y
            else:
                self._warehouse[(n_x, n_y)] = symbol
                self._warehouse[(x, y)] = _empty
                return n_x, n_y

    def _move_wide(self, position: tuple[int, int], move: tuple[int, int], is_safe: bool = False) -> tuple[int, int]:
        x, y = position
        dx, dy = move
        next_move = (x + dx, y + dy)
        symbol = self._warehouse[(x, y)]
        if (is_safe or self.is_move_wide_possible(position, move)) and symbol != _empty:
            is_horizontal = dy == 0
            if is_horizontal or symbol == _robot:
                self._move_wide(next_move, move, True)
                self._warehouse[next_move] = symbol
                self._warehouse[position] = _empty
            else:
                next_moves = [(x + dx, y + dy), (x + dx + (1 if symbol == _box_left else -1), y + dy)]
                for n_x, n_y in next_moves:
                    self._move_wide((n_x, n_y), move, True)
                    self._warehouse[(n_x, n_y)] = self._warehouse[(n_x - dx, n_y - dy)]
                    self._warehouse[(n_x - dx, n_y - dy)] = _empty
            return next_move
        else:
            return position

    def is_move_wide_possible(self, position: tuple[int, int], move: tuple[int, int]) -> bool:
        dx, dy = move
        queue = deque([position])
        while queue:
            x, y = queue.popleft()
            symbol = self._warehouse[(x, y)]
            if symbol == _wall:
                return False
            elif symbol == _empty:
                continue
            elif symbol in {_box_left, _box_right}:
                if dy == 0:
                    queue.append((x + 2 * dx, y + dy))
                else:
                    queue.append((x + dx, y + dy))
                    queue.append((x + dx + (1 if symbol == _box_left else -1), y + dy))
            else:
                queue.append((x + dx, y + dy))
        return True

    def get_boxes_coordinates_sum(self) -> int:
            return sum([100 * y + x for x, y in self._warehouse.find(_box_left if self._is_wide else _box)])
