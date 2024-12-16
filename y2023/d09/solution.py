class Sensor:
    def __init__(self, lines: list[str]):
        reports = [Report(list(map(int, line.split(" ")))) for line in lines]
        self._reports = reports

    def get_extrapolated_values_sum(self):
        return sum([report.get_next_value() for report in self._reports])

    def get_extrapolated_previous_values_sum(self):
        return sum([report.get_previous_value() for report in self._reports])

class Report:
    def __init__(self, values: list[int]):
        self._values = values

    def _get_levels(self):
        levels = [self._values]
        current = self._values

        while any(value != 0 for value in current):
            prev = current[0]
            next_level = []
            for value in current[1:]:
                next_level.append(value - prev)
                prev = value
            levels.append(next_level)
            current = next_level
        return levels

    def get_next_value(self):
        levels = self._get_levels()
        return sum([level[-1] for level in levels])

    def get_previous_value(self):
        levels = self._get_levels()
        total = 0
        for values in reversed(levels):
            total = values[0] - total
        return total