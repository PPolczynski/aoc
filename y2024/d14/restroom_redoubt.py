import math
import re
from functools import reduce

from utils.matrix import Matrix


class RestroomRedoubt:
    def __init__(self, robots: list[str], length_x: int, length_y: int):
        self._robots = [
            (tuple(map(int, re.findall("\d+", position))),
             tuple(map(int, re.findall("-?\d+", velocity))))
            for position, velocity in [robot.split(" ") for robot in robots]]
        self._length_x = length_x
        self._length_y = length_y

    def pass_time(self, seconds: int) -> None:
        for idx, robot in enumerate(self._robots):
            position, velocity = robot
            x, y = position
            v_x, v_y = velocity
            self._robots[idx] = (((x + v_x * seconds) % self._length_x, (y + v_y * seconds) % self._length_y), velocity)
        pass

    def get_safety_factor(self) -> int:
        middle_x = math.ceil(self._length_x / 2) - 1
        middle_y = math.ceil(self._length_y / 2) - 1
        quadrants = {
            (0, middle_x, 0 , middle_y) : 0,
            (middle_x + 1, self._length_x, 0, middle_y) : 0,
            (0, middle_x, middle_y + 1, self._length_y): 0,
            (middle_x + 1, self._length_x, middle_y + 1, self._length_y): 0,
        }
        for position, _ in self._robots:
            x, y = position
            for x_start, x_end, y_start, y_end in quadrants.keys():
                if x_start <= x < x_end and y_start <= y < y_end:
                    quadrants[(x_start, x_end, y_start, y_end)] += 1
        return reduce(lambda a, b: a * b, quadrants.values())

    def print_robots(self):
        empty = Matrix.get_empty(self._length_x, self._length_y, ".")
        for robot in self._robots:
             empty[robot[0]] = "1" if empty[robot[0]] == "." else str(int(empty[robot[0]]) + 1)
        print("***")
        print(empty)
        print("***")