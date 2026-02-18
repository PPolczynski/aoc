import time
from .event import Event
from .solution import Solution

class Solver:
    def __init__(self, client):
        self._client = client
        self._events = {}

    def register(self, event: Event):
        self._events[event.get_year()] = event

    def solve(self, year: str | None = None, day: str | None = None):
        if not year and not day:
            for y in sorted(self._events.keys()):
                self._solve_year(self._events[y])
            return

        if year not in self._events:
            print(f"year {year} not implemented")
            return

        y = self._events[year]
        if not day:
            self._solve_year(y)
            return

        d = y.get_day(day)
        if d is None:
            print(f"day {day} in year {year} not implemented")
            return

        print(f"Year {year}")
        self._solve_day(d)

    def _solve_year(self, event: Event):
        print(f"Year {event.get_year()}")
        for d in event.get_solutions():
            self._solve_day(d)

    def _solve_day(self, day: Solution):
        d, y = day.date()
        input_data = self._client.get(y, d)
        if input_data is None:
            return

        input_data = self._normalize(input_data)
        print(f"Day {d}: {day.subject()}")
        self._solve_part("Part 1", input_data, day.part1)
        self._solve_part("Part 2", input_data, day.part2)

    @staticmethod
    def _solve_part(name: str, input_data: str, part_func):
        start = time.time()
        try:
            value = part_func(input_data)
            duration = time.time() - start
            print(f"[{name}]: {value} time: {duration:.6f}s")
        except Exception as e:
            print(f"[{name}] error: {e}")

    @staticmethod
    def _normalize(i: str) -> str:
        return i#.replace(""").strip("")
