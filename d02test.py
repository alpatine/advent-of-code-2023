from unittest import TestCase
from d02p1 import d02p1
from d02p2 import d02p2

class Day02_Test(TestCase):
    def test_part1_example1(self):
        raw_data = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''
        self.assertEqual(d02p1(raw_data), 8)

    def test_part1_solution(self):
        self.assertEqual(d02p1(), 2256)

    def test_part2_example1(self):
        raw_data = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''
        self.assertEqual(d02p2(raw_data), 2286)

    def test_part2_solution(self):
        self.assertEqual(d02p2(), 74229)
