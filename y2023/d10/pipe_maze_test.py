import unittest

from y2023.d10.pipe_maze import PipeMaze


class PipeMazeTestCase(unittest.TestCase):
    def test_get_furthest_step1(self):
        maze = [
            ".....",
            ".S-7.",
            ".|.|.",
            ".L-J.",
            "....."
        ]
        pipe_maze = PipeMaze(maze)
        self.assertEqual(4, pipe_maze.get_furthest_step())

    def test_get_furthest_step2(self):
        maze = [
            "..F7.",
            ".FJ|.",
            "SJ.L7",
            "|F--J",
            "LJ..."
        ]
        pipe_maze = PipeMaze(maze)
        self.assertEqual(8, pipe_maze.get_furthest_step())

    def test_get_furthest_step3(self):
        maze = [
            "7-F7-",
            ".FJ|7",
            "SJLL7",
            "|F--J",
            "LJ.LJ"
        ]
        pipe_maze = PipeMaze(maze)
        self.assertEqual(8, pipe_maze.get_furthest_step())

    def test_get_enclosed_tile_count1(self):
        maze = [
            "...........",
            ".S-------7.",
            ".|F-----7|.",
            ".||.....||.",
            ".||.....||.",
            ".|L-7.F-J|.",
            ".|..|.|..|.",
            ".L--J.L--J.",
            "..........."
        ]
        pipe_maze = PipeMaze(maze)
        self.assertEqual(4, pipe_maze.get_enclosed_tile_count())

    def test_get_enclosed_tile_count2(self):
        maze = [
            "..........",
            ".S------7.",
            ".|F----7|.",
            ".||....||.",
            ".||....||.",
            ".|L-7F-J|.",
            ".|..||..|.",
            ".L--JL--J.",
            ".........."
        ]
        pipe_maze = PipeMaze(maze)
        self.assertEqual(4, pipe_maze.get_enclosed_tile_count())

    def test_get_enclosed_tile_count3(self):
        maze = [
            ".F----7F7F7F7F-7....",
            ".|F--7||||||||FJ....",
            ".||.FJ||||||||L7....",
            "FJL7L7LJLJ||LJ.L-7..",
            "L--J.L7...LJS7F-7L7.",
            "....F-J..F7FJ|L7L7L7",
            "....L7.F7||L7|.L7L7|",
            ".....|FJLJ|FJ|F7|.LJ",
            "....FJL-7.||.||||...",
            "....L---J.LJ.LJLJ..."
        ]
        pipe_maze = PipeMaze(maze)
        self.assertEqual(8, pipe_maze.get_enclosed_tile_count())

    def test_get_enclosed_tile_count4(self):
        maze = [
            "FF7FSF7F7F7F7F7F---7",
            "L|LJ||||||||||||F--J",
            "FL-7LJLJ||||||LJL-77",
            "F--JF--7||LJLJ7F7FJ-",
            "L---JF-JLJ.||-FJLJJ7",
            "|F|F-JF---7F7-L7L|7|",
            "|FFJF7L7F-JF7|JL---7",
            "7-L-JL7||F7|L7F-7F7|",
            "L.L7LFJ|||||FJL7||LJ",
            "L7JLJL-JLJLJL--JLJ.L"
        ]
        pipe_maze = PipeMaze(maze)
        self.assertEqual(10, pipe_maze.get_enclosed_tile_count())


if __name__ == '__main__':
    unittest.main()
