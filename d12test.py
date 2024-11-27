from unittest import TestCase

from d12p1 import d12p1
from d12p2 import d12p2


class Day12_Test(TestCase):
    def test_part1_example(self):
        data = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
'''
        self.assertEqual(d12p1(data), 21)
    
    def test_part1_solution(self):
        self.assertEqual(d12p1(), 7379)

    def test_part2_example(self):
        data = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
'''
        self.assertEqual(d12p2(data), 525152)

    def test_part2_solution(self):
        self.assertEqual(d12p2(), 7732028747925)
