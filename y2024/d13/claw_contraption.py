import re

_max_button_press = 100
_a_press_price = 3
_b_press_price = 1

class ClawContraption:
    def __init__(self, machines: list[list[str]]):
        self._machines = [ClawMachine(machine, _a_press_price, _b_press_price, _max_button_press) for machine in machines]

    def get_fewest_token_to_win(self):
        return sum(machine.get_min_token_to_win() for machine in self._machines)

    def get_fewest_token_to_win_with_conversion(self, price_position_conversion: int):
        return sum(machine.get_min_token_to_win(price_position_conversion, False) for machine in self._machines)

class ClawMachine:
    def __init__(self, machine: list[str], a_press_price: int, b_press_price: int, button_press_limit: int):
        self._button_a = tuple(map(int, re.findall("\d+", machine[0])))
        self._button_b = tuple(map(int, re.findall("\d+", machine[1])))
        self._prize= tuple(map(int, re.findall("\d+", machine[2])))
        self._a_press_price = a_press_price
        self._b_press_price = b_press_price
        self._button_press_limit = button_press_limit

    def get_min_token_to_win(self, price_position_conversion: int = 0, is_limited: bool = True) -> int:
        t_x, t_y = self._prize
        t_x, t_y = t_x + price_position_conversion, t_y + price_position_conversion
        a_x, a_y = self._button_a
        b_x, b_y = self._button_b
        # n - times press A
        # m - times press B
        div = (a_y * b_x - a_x * b_y)
        if div == 0:
            return 0
        n = (t_y * b_x - t_x * b_y) / div
        m = (t_x - n * a_x) / b_x
        if (n.is_integer() and m.is_integer() and
            (not is_limited or n <= self._button_press_limit and m <= self._button_press_limit)):
            return int(n * self._a_press_price + m * self._b_press_price)
        return 0

    def __str__(self):
        return f"A: {self._button_a} B: {self._button_b}, prize: {self._prize}"