import unittest

from y2024.d13.claw_contraption import ClawContraption


class MyTestCase(unittest.TestCase):
    def test_get_min_token_to_win(self):
        machines = [
            [
            "Button A: X+94, Y+34",
            "Button B: X+22, Y+67",
            "Prize: X=8400, Y=5400"
            ], [
            "Button A: X+26, Y+66",
            "Button B: X+67, Y+21",
            "Prize: X=12748, Y=12176"
            ], [
            "Button A: X+17, Y+86",
            "Button B: X+84, Y+37",
            "Prize: X=7870, Y=6450"
            ], [
            "Button A: X+69, Y+23",
            "Button B: X+27, Y+71",
            "Prize: X=18641, Y=10279"
            ]
        ]
        claw_contraption = ClawContraption(machines)
        self.assertEqual(480, claw_contraption.get_fewest_token_to_win())

    def test_get_fewest_token_to_win_with_conversion(self):
        machines = [
            [
            "Button A: X+94, Y+34",
            "Button B: X+22, Y+67",
            "Prize: X=8400, Y=5400"
            ], [
            "Button A: X+26, Y+66",
            "Button B: X+67, Y+21",
            "Prize: X=12748, Y=12176"
            ], [
            "Button A: X+17, Y+86",
            "Button B: X+84, Y+37",
            "Prize: X=7870, Y=6450"
            ], [
            "Button A: X+69, Y+23",
            "Button B: X+27, Y+71",
            "Prize: X=18641, Y=10279"
            ]
        ]
        claw_contraption = ClawContraption(machines)
        self.assertEqual(875318608908, claw_contraption.get_fewest_token_to_win_with_conversion(10000000000000))

if __name__ == '__main__':
    unittest.main()