from unittest import TestCase
from d03p1 import d03p1
from d03p2 import d03p2

class Day03_Test(TestCase):
    def test_part1_example1(self):
        raw_data = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''
        self.assertEqual(d03p1(raw_data), 4361)
    
    def test_part1_solution(self):
        self.assertEqual(d03p1(), 537832)
    
    def test_part2_example1(self):
        raw_data = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''
        self.assertEqual(d03p2(raw_data), 467835)
    
    def test_part2_solution(self):
        self.assertEqual(d03p2(), 81939900)
