from typing import Callable

def _not_implemented(*arg):
    raise NotImplementedError()


class Solution():
    def __init__(self, 
                 subject: str, 
                 day: str, 
                 year: str, 
                 part1:Callable = _not_implemented, 
                 part2:Callable = _not_implemented,
                 part1_preprocess : Callable|None = None,
                 part2_preprocess : Callable|None = None,
                 ):
        self._subject = subject
        self._day = day
        self._year = year
        self._part1_func = part1
        self._part2_func = part2
        self._part1_preprocess = part1_preprocess
        self._part2_preprocess = part2_preprocess

    def date(self) -> tuple[str, str]:
        return self._day, self._year

    def subject(self) -> str:
        return self._subject

    def part1(self, input_data: str) -> any:
        if self._part1_preprocess:
            input_data = self._part1_preprocess(input_data)
        return self._part1_func(input_data)

    def part2(self, input_data: str) -> any:
        if self._part2_preprocess:
            input_data = self._part2_preprocess(input_data)
        return self._part2_func(input_data)
