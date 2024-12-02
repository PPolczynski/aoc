_MAX_DIFFERENCE = 3

class RedNosedReports:
    def __init__(self, reports: list[list[int]]):
        self._reports = reports

    def get_safe_levels_count(self) -> int:
        return sum([1 if self._is_report_safe(report) else 0 for report in self._reports])

    @staticmethod
    def _is_report_safe(report: list[int]) -> bool:
        if not len(report) or len(report) == 1:
            return True
        direction = report[1] - report[0]
        previous = report[0]
        for level in report[1:]:
            diff = level - previous
            if diff == 0 or (diff > 0 > direction) or (diff < 0 < direction) or abs(diff) > _MAX_DIFFERENCE:
                return False
            previous = level
        return True