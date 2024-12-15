from utils.matrix import Matrix

_wall = "#"
_box = "O"
_robot = "@"
_empty = "."

_moves = {
    "^" : (0, -1),
    ">" : (1, 0),
    "v" : (0, 1),
    "<" : (-1, 0)
}

class WarehouseWoes:
    def __init__(self, warehouse):
        self._warehouse = Matrix(warehouse, _wall)

    def apply_moves(self, move_groups: list[str]) -> None:
        robot_position = self._warehouse.find(_robot)[0]
        for moves in move_groups:
            for move in moves:
                robot_position = self._move(robot_position, _moves[move])


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

    def get_boxes_coordinates_sum(self) -> int:
        return sum([100 * y + x for x, y in self._warehouse.find(_box)])