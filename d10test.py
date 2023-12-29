from unittest import TestCase

from d10p1 import d10p1


class Day10_Test(TestCase):
    def test_part1_example1(self):
        raw_data = '''-L|F7
7S-7|
L|7||
-L-J|
L|-JF'''
        self.assertEqual(d10p1(raw_data), 4)
    
    def test_part1_example2(self):
        raw_data = '''7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ'''
        self.assertEqual(d10p1(raw_data), 8)
    
    def test_part1_solution(self):
        self.assertEqual(d10p1(), 7097)
