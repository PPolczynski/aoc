from unittest import TestCase

from utils.range import Range
from y2023.d19.solution import PartRange, Workflow, Rule, Operation


class TestPartRange(TestCase):
    def test_split(self):
        first = PartRange({"x": Range(1, 4000)})
        self.assertListEqual(first.split("x", 2000),
                             [PartRange({"x": Range(1, 2000)}), PartRange({"x": Range(2001, 4000)})])
        first = PartRange({"x": Range(1, 4000), "m": Range(2, 3000)})
        self.assertListEqual(first.split("x", 2000),
                             [PartRange({"x": Range(1, 2000), "m": Range(2, 3000)}),
                              PartRange({"x": Range(2001, 4000), "m": Range(2, 3000)})])


class TestWorkflow(TestCase):
    def test_resolve_range(self):
        workflow1 = Workflow(label="", rules=[Rule(field="m", operation=Operation.GREATER, value=50, outcome="A"),
                                              Rule(field="", operation=Operation.NONE, value=0, outcome="R")])
        range1 = PartRange({"m": Range(1, 100)})
        self.assertListEqual(sorted(workflow1.resolve_range(range1)),
                             sorted([("R", PartRange({"m": Range(1, 50)})), ("A", PartRange({"m": Range(51, 100)}))]))


class TestRule(TestCase):
    def test_apply_over_range(self):
        r1 = Rule(field="", operation=Operation.NONE, value=0, outcome="A")
        range1 = PartRange({"m": Range(1, 100)})
        self.assertListEqual(r1.apply_over_range(range1), [(True, "A", range1)])
        r2 = Rule(field="m", operation=Operation.GREATER, value=50, outcome="R")
        self.assertListEqual(r2.apply_over_range(range1), [(False, "", PartRange({"m": Range(1, 50)})),
                                                           (True, "R", PartRange({"m": Range(51, 100)}))])
        r3 = Rule(field="m", operation=Operation.SMALLER, value=50, outcome="R")
        self.assertListEqual(r3.apply_over_range(range1), [(True, "R", PartRange({"m": Range(1, 49)})),
                                                           (False, "", PartRange({"m": Range(50, 100)}))])
        r4 = Rule(field="m", operation=Operation.GREATER, value=100, outcome="R")
        self.assertListEqual(r4.apply_over_range(range1), [(False, "", range1)])
        r5 = Rule(field="m", operation=Operation.GREATER, value=10, outcome="R")
        range2 = PartRange({"m": Range(10, 100)})
        self.assertListEqual(r5.apply_over_range(range2), [(False, "", PartRange({"m": Range(10, 10)})),
                                                           (True, "R", PartRange({"m": Range(11, 100)}))])
        r6 = Rule(field="m", operation=Operation.GREATER, value=8, outcome="R")
        self.assertListEqual(r6.apply_over_range(range2), [(True, "R", range2)])
        r7 = Rule(field="m", operation=Operation.SMALLER, value=101, outcome="A")
        self.assertListEqual(r7.apply_over_range(range2), [(True, "A", range2)])
        r8 = Rule(field="m", operation=Operation.SMALLER, value=100, outcome="A")
        self.assertListEqual(r8.apply_over_range(range2), [(True, "A", PartRange({"m": Range(10, 99)})),
                                                           (False, "", PartRange({"m": Range(100, 100)}))])
        r9 = Rule(field="m", operation=Operation.SMALLER, value=10, outcome="A")
        self.assertListEqual(r9.apply_over_range(range2), [(False, "", range2)])
