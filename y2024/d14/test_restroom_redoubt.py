from unittest import TestCase

from y2024.d14.restroom_redoubt import RestroomRedoubt


class TestRestroomRedoubt(TestCase):
    def test_get_safety_factor(self):
        robots = [
            "p=0,4 v=3,-3",
            "p=6,3 v=-1,-3",
            "p=10,3 v=-1,2",
            "p=2,0 v=2,-1",
            "p=0,0 v=1,3",
            "p=3,0 v=-2,-2",
            "p=7,6 v=-1,-3",
            "p=3,0 v=-1,-2",
            "p=9,3 v=2,3",
            "p=7,3 v=-1,2",
            "p=2,4 v=2,-3",
            "p=9,5 v=-3,-3"
        ]
        restroom_redoubt = RestroomRedoubt(robots, 11, 7)
        restroom_redoubt.pass_time(100)
        self.assertEqual(12, restroom_redoubt.get_safety_factor())
