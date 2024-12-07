import unittest

from y2023.d08.haunted_wasteland import HauntedWasteland


class HauntedWastelandTestCase(unittest.TestCase):
    def test_get_steps_count(self):
        lines = [
                "RL",
                "",
                "AAA = (BBB, CCC)",
                "BBB = (DDD, EEE)",
                "CCC = (ZZZ, GGG)",
                "DDD = (DDD, DDD)",
                "EEE = (EEE, EEE)",
                "GGG = (GGG, GGG)",
                "ZZZ = (ZZZ, ZZZ)"
                ]

        haunted_wasteland = HauntedWasteland(lines[2:])
        self.assertEqual(2, haunted_wasteland.get_steps_count(lines[0]))
        lines2 = [
                "LLR",
                "",
                "AAA = (BBB, BBB)",
                "BBB = (AAA, ZZZ)",
                "ZZZ = (ZZZ, ZZZ)"
                ]

        haunted_wasteland2 = HauntedWasteland(lines2[2:])
        self.assertEqual(6, haunted_wasteland2.get_steps_count(lines2[0]))

    def test_get_steps_count_ghost(self):
        lines = [
                "LR",
                "",
                "11A = (11B, XXX)",
                "11B = (XXX, 11Z)",
                "11Z = (11B, XXX)",
                "22A = (22B, XXX)",
                "22B = (22C, 22C)",
                "22C = (22Z, 22Z)",
                "22Z = (22B, 22B)",
                "XXX = (XXX, XXX)"
                ]
        haunted_wasteland = HauntedWasteland(lines[2:])
        self.assertEqual(6, haunted_wasteland.get_steps_count_ghost(lines[0]))

if __name__ == '__main__':
    unittest.main()
