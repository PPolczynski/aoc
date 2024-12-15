from unittest import TestCase

from y2023.d16.the_floor_wil_be_lava import TheFloorWillBeLava


class TestTheFloorWillBeLava(TestCase):
    def test_get_energized_tiles_count(self):
        contraption = [
            ".|...\....",
            "|.-.\.....",
            ".....|-...",
            "........|.",
            "..........",
            ".........\\",
            "..../.\\\\..",
            ".-.-/..|..",
            ".|....-|.\\",
            "..//.|....",
        ]
        the_floor_wil_be_lava = TheFloorWillBeLava(contraption)
        self.assertEqual(46, the_floor_wil_be_lava.get_energized_tiles_count((0,0), (1,0)))

    def test_get_max_energized_tiles_count(self):
        contraption = [
            ".|...\....",
            "|.-.\.....",
            ".....|-...",
            "........|.",
            "..........",
            ".........\\",
            "..../.\\\\..",
            ".-.-/..|..",
            ".|....-|.\\",
            "..//.|....",
        ]
        the_floor_wil_be_lava = TheFloorWillBeLava(contraption)
        self.assertEqual(51, the_floor_wil_be_lava.get_energized_tiles_count((3, 0), (0, 1)))
        self.assertEqual(51, the_floor_wil_be_lava.get_max_energized_tiles_count())
