from functools import reduce
from itertools import chain


raw_data = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''

# Comment file read to use sample data above
with open('d05data.txt') as file:
    raw_data = file.read()

class Range:
    def __init__(self, start, end, offset = None) -> None:
        self.start = start
        self.end = end
        self.offset = offset or 0
    
    def __repr__(self) -> str:
        return f'({self.start},{self.end},{self.offset})'
    
    def intersect(self, range):
        start = max(self.start, range.start)
        end = min(self.end, range.end)
        if start <= end:
            return Range(start, end, 0)
        else:
            return None

class Map:
    def __init__(self, block) -> None:
        self.ranges = []
        for block_line in block[1:]:
            numbers = [int(number) for number in block_line.split()]
            range_start = numbers[1]
            range_end = numbers[1] + numbers[2] - 1
            range_offset = numbers[0] - numbers[1]
            self.ranges.append(Range(range_start, range_end, range_offset))
    
    def map_ranges(self, source_ranges):
        targets = []
        for range in self.ranges:    
            unmatched = []
            for source in source_ranges:
                intersection = source.intersect(range)
                if intersection is not None:
                    if source.start < intersection.start:
                        unmatched.append(Range(source.start, intersection.start-1, 0))
                    targets.append(Range(intersection.start + range.offset, intersection.end + range.offset, 0))
                    if source.end > intersection.end:
                        unmatched.append(Range(intersection.end+1, source.end, 0))
                else:
                    unmatched.append(source)
            source_ranges = unmatched
        targets.extend(unmatched)
        return targets

# map input into blocks
blocks = [[]]
current_block = blocks[0]

for line in raw_data.splitlines():
    if line != '':
        current_block.append(line)
    else: 
        current_block = []
        blocks.append(current_block)

# pairwise iterator - returns elements two at a time, no overlap
def pairwise(iterable):
    i = iter(iterable)
    return zip(i, i)

# The first block is the list of seed ranges (start, length) to be mapped
ranges = []    
seed_range_values = [int(number) for number in blocks[0][0].split()[1:]]
for start, length in pairwise(seed_range_values):
    ranges.append(Range(start, start+length-1, 0))

# The remaining blocks are range maps
range_maps = [Map(block) for block in blocks[1:]]

# Apply the maps in order to each seed
for map in range_maps:
    ranges = map.map_ranges(ranges)

print(min([range.start for range in ranges]))
