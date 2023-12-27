from unittest import TestCase
from d01p1 import d01p1
from d01p2 import d01p2

class Day01_Test(TestCase):
    def test_part1_example1(self):
        raw_data = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''
        self.assertEqual(d01p1(raw_data), 142)
    
    def test_part1_solution(self):
        self.assertEqual(d01p1(), 55447)

    def test_part2_example1(self):
        raw_data = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''
        self.assertEqual(d01p2(raw_data), 281)
    
    def test_part2_solution(self):
        self.assertEqual(d01p2(), 54706)
