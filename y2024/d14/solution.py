import math
import re
from functools import reduce
from utils.matrix import Matrix
from puzzle import Solution

def _preprocess(input_data: str) -> list[str]:
    return input_data.splitlines()

def _part1(lines: list[str]) -> any:
    robots = Robots(lines, 101, 103)
    robots.pass_time(100)
    return robots.get_safety_factor()

def _part2(lines: list[str]) -> any:
    robots = Robots(lines, 101, 103)
    # Change to True to see the tree
    return robots.search_for_christmas_tree(3, False)

solution = Solution(
    "Restroom Redoubt",
    "14",
    "2024",
    part1=_part1,
    part2=_part2,
    part1_preprocess=_preprocess,
    part2_preprocess=_preprocess
)

class Robots:
    def __init__(self, robots: list[str], length_x: int, length_y: int):
        self._robots = [
            (tuple(map(int, re.findall(r"\d+", position))),
             tuple(map(int, re.findall(r"-?\d+", velocity))))
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

    def search_for_christmas_tree_manual(self):
        cnt = 0
        while True:
            self.pass_time(1)
            cnt += 1
            print(f"****** time passed: {cnt} ******")
            self.print_robots()
            is_continue = input("continue ? (any/N)")
            if is_continue == "N":
                break

    def search_for_christmas_tree(self, min_expected_levels : int, should_print: bool):
        time_passed = 0
        while True:
            found_candidate = False
            self.pass_time(1)
            time_passed += 1
            robots = set([position for position, _ in self._robots])
            for robot in robots:
                potential_robots = [robot]
                level = 0
                while level < min_expected_levels:
                   if not all(potential_robot in robots for potential_robot in potential_robots):
                       break #we break from while and continue for next robot
                   next_level = set()
                   for x, y in potential_robots:
                       next_level.add((x - 1, y + 1))
                       next_level.add((x, y + 1))
                       next_level.add((x + 1, y + 1))
                   potential_robots = list(next_level)
                   level += 1
                else:
                    found_candidate = True
                    break # we have a candidate
            if found_candidate:
                if should_print:
                    print(f"****** time passed: {time_passed} ******")
                    self.print_robots()
                    is_continue = input("continue ? (Y/any)")
                    if is_continue != "Y":
                        break
                return time_passed

    def print_robots(self):
        empty = Matrix.get_empty(self._length_x, self._length_y, ".")
        for robot in self._robots:
             empty[robot[0]] = "*"
        print(empty)