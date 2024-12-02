import unittest

from y2023.d02.cube_conundrum import CubeConundrum


class CubeConundrumCase(unittest.TestCase):
    def test_get_sum_possible_id(self):
        records = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
                    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
                    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
                    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
                    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
        cube_conundrum = CubeConundrum([("red", 12), ("green", 13), ("blue", 14)])

        self.assertEqual(cube_conundrum.get_sum_possible_id(records), 8)

    def test_get_sum_of_power(self):
        records = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
                    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
                    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
                    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
                    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
        cube_conundrum = CubeConundrum([("red", 12), ("green", 13), ("blue", 14)])

        self.assertEqual(cube_conundrum.get_sum_of_power(records), 2286)

if __name__ == '__main__':
    unittest.main()
