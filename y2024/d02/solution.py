from puzzle import Solution

_MAX_DIFFERENCE = 3

def _preprocess(input_data: str) -> list[list[int]]:
    return [[int(level) for level in line.split()] for line in input_data.splitlines()]

def _part1(reports: list[list[int]]) -> any:
    reactor_reports = ReactorReports(reports)
    return reactor_reports.get_safe_reports_count()

def _part2(reports: list[list[int]]) -> any:
    reactor_reports = ReactorReports(reports)
    return reactor_reports.get_safe_reports_count_with_tolerance()

solution = Solution(
    "Red-Nosed Reports",
    "2",
    "2024",
    part1=_part1,
    part2=_part2,
    part1_preprocess=_preprocess,
    part2_preprocess=_preprocess
)

class ReactorReports:
    def __init__(self, reports: list[list[int]]):
        self._reports = reports

    def get_safe_reports_count(self) -> int:
        return sum([1 if self._is_report_safe(report) else 0 for report in self._reports])

    def get_safe_reports_count_with_tolerance(self) -> int:
        return sum([1 if self._is_report_safe_tolerance(report) else 0 for report in self._reports])

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

    @staticmethod
    def _is_report_safe_tolerance(report: list[int]) -> bool:
        return (ReactorReports._is_report_safe(report)
                or any([ReactorReports._is_report_safe(report[:i] + report[i + 1:]) for i, _ in enumerate(report)]))