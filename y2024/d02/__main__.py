import time

from y2024.d02.solution import ReactorReports

if __name__ == '__main__':
    reports = []
    split_characters = " "
    with open("data", "r") as data_file:
        for line in data_file:
            values = line.rstrip().split(split_characters)
            reports.append([int(level) for level in values])
    reactor_reports = ReactorReports(reports)
    print("Part 1:")
    start = time.time()
    print(f"{reactor_reports.get_safe_reports_count()} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{reactor_reports.get_safe_reports_count_with_tolerance()} time: {time.time() - start}s")