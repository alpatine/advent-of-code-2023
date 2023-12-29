from unittest import TestCase

from d09p1 import d09p1
from d09p2 import d09p2


class Day09_Test(TestCase):
    def test_part1_example1(self):
        raw_data = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''
        self.assertEqual(d09p1(raw_data), 114)
    
    def test_part1_solution(self):
        self.assertEqual(d09p1(), 1731106378)

    def test_part2_example1(self):
        raw_data = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''
        self.assertEqual(d09p2(raw_data), 2)
    
    def test_part2_solution(self):
        self.assertEqual(d09p2(), 1087)
