import unittest

from y2024.d06.guard_gallivant import GuardGallivant

maze = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#..."
]

class GuardGallivantTestCase(unittest.TestCase):
    def test_get_guard_move_count(self):
        guard_gallivant = GuardGallivant(maze)
        self.assertEqual(guard_gallivant.get_guard_move_count(), 41)

    def test_get_possible_loop_count(self):
        guard_gallivant = GuardGallivant(maze)
        self.assertEqual(guard_gallivant.get_possible_loop_count(), 6)

    def test_get_possible_loop_count_1(self):
        maze_l = ["..#.",
                "...#",
                "..^."]
        guard_gallivant = GuardGallivant(maze_l)
        self.assertEqual(guard_gallivant.get_possible_loop_count(), 0)

    def test_get_possible_loop_count_2(self):
        maze_l = [
            ".#.",
            "#.#",
            "#^.",
            "..."
        ]
        guard_gallivant = GuardGallivant(maze_l)
        self.assertEqual(guard_gallivant.get_possible_loop_count(), 1)

    def test_get_possible_loop_count_3(self):
        maze_l = [
            ".#.",
            "..#",
            "#^.",
            "..."
        ]
        guard_gallivant = GuardGallivant(maze_l)
        self.assertEqual(guard_gallivant.get_possible_loop_count(), 1)

    def test_get_possible_loop_count_4(self):
        maze_l = [
            ".##.",
            "#..#",
            "....",
            "..^."
        ]
        guard_gallivant = GuardGallivant(maze_l)
        self.assertEqual(guard_gallivant.get_possible_loop_count(), 0)

if __name__ == '__main__':
    unittest.main()
