from unittest import TestCase
from d08p1 import d08p1
from d08p2 import d08p2

class Day08_Test(TestCase):
    def test_part1_example1(self):
        raw_data = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)'''
        self.assertEqual(d08p1(raw_data), 2)
    
    def test_part1_example2(self):
        raw_data = '''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)'''
        self.assertEqual(d08p1(raw_data), 6)
    
    def test_part1_solution(self):
        self.assertEqual(d08p1(), 20659)

    def test_part2_example1(self):
        raw_data = '''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)'''
        self.assertEqual(d08p2(raw_data), 6)

    def test_part2_solution(self):
        self.assertEqual(d08p2(), 15690466351717)
