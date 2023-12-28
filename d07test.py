from unittest import TestCase
from d07p1 import d07p1
from d07p2 import d07p2

class Day07_Test(TestCase):
    def test_part1_example1(self):
        raw_data = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''
        self.assertEqual(d07p1(raw_data), 6440)
    
    def test_part1_solution(self):
        self.assertEqual(d07p1(), 251287184)
    
    def test_part2_example1(self):
        raw_data = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''
        self.assertEqual(d07p2(raw_data), 5905)
    
    def test_part2_solution(self):
        self.assertEqual(d07p2(), 250757288)
