from y2023.d01.trebuchet import Trebuchet

if __name__ == '__main__':
    document = []
    with open("data", "r") as data_file:
        for line in data_file:
            document.append(line.rstrip())
    trebuchet = Trebuchet(document)
    print("What is the sum of all of the calibration values?")
    print(trebuchet.get_calibration())
    print("What is the sum of all of the calibration values? (spelled out numbers)")
    print(trebuchet.get_calibration_spelled_out())