from d02.red_nosed_reports import RedNosedReports

if __name__ == '__main__':
    reports = []
    split_characters = " "
    with open("data", "r") as data_file:
        for line in data_file:
            values = line.rstrip().split(split_characters)
            reports.append([int(level) for level in values])
    red_nosed_reports = RedNosedReports(reports)
    print("How many reports are safe?")
    print(red_nosed_reports.get_safe_reports_count())
    print("How many reports are now safe?")
    print(red_nosed_reports.get_safe_reports_count_with_tolerance())