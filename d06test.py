from unittest import TestCase
from d06p1 import d06p1
from d06p2 import d06p2

class Day06_Test(TestCase):
    def test_part1_example1(self):
        raw_data = '''Time:      7  15   30
Distance:  9  40  200'''
        self.assertEqual(d06p1(raw_data), 288)
    
    def test_part1_solution(self):
        self.assertEqual(d06p1(), 3316275)
    
    def test_part2_example1(self):
        raw_data = '''Time:      7  15   30
Distance:  9  40  200'''
        self.assertEqual(d06p2(raw_data), 71503)
    
    def test_part2_solution(self):
        self.assertEqual(d06p2(), 27102791)
