import unittest

from y2023.d01.trebuchet import Trebuchet


class TrebuchetCase(unittest.TestCase):
    def test_get_calibration(self):
        document = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
        trebuchet = Trebuchet(document)
        self.assertEqual(trebuchet.get_calibration(), 142)

    def test_get_calibration_spelled_out(self):
        document = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four",
                    "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
        trebuchet = Trebuchet(document)
        self.assertEqual(trebuchet.get_calibration_spelled_out(), 281)

if __name__ == '__main__':
    unittest.main()
