from unittest import TestCase

from d11p1 import d11p1


class Day11_Test(TestCase):
    def test_part1_example1(self):
        data = '''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....'''
        self.assertEqual(d11p1(data), 374)

    def test_part1_solution(self):
        self.assertEqual(d11p1(), 9445168)
