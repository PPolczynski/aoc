from .solution import Solution

class Event():
    def __init__(self, solutions: list[Solution], year:str=None):
        self._solutions = solutions
        if year:
            self._year = year
        elif solutions:
            _, year = solutions[0].date()
            self._year = year
        else:
            self._year = ""
        self._map = dict()
        for s in self._solutions:
            d, _ = s.date()
            self._map[d] = s

    def get_year(self) -> str:
        return self._year

    def get_solutions(self) -> list[Solution]:
        return self._solutions

    def get_day(self, day: str) -> Solution | None:
        if day in self._map:
            return self._map[day]
        return None