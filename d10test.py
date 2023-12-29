from unittest import TestCase

from d10p1 import d10p1
from d10p2 import d10p2


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
    
    def test_part2_example1(self):
        raw_data = '''...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........'''
        self.assertEqual(d10p2(raw_data), 4)
    
    def test_part2_example2(self):
        raw_data = '''..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
..........'''
        self.assertEqual(d10p2(raw_data), 4)

    def test_part2_example3(self):
        raw_data = '''.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...'''
        self.assertEqual(d10p2(raw_data), 8)

    def test_part2_example4(self):
        raw_data = '''FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L'''
        self.assertEqual(d10p2(raw_data), 10)

    def test_part2_solution(self):
        self.assertEqual(d10p2(), 355)
