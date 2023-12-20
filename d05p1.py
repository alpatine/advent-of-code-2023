from functools import reduce


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
    def __init__(self, start, offset, length) -> None:
        self.start = start
        self.offset = offset
        self.length = length
    
    def contains(self, source):
        return source >= self.start and source <= (self.start + self.length - 1)

class Map:
    def __init__(self, block) -> None:
        self.ranges = []
        for block_line in block[1:]:
            numbers = [int(number) for number in block_line.split()]
            range_start = numbers[1]
            range_offset = numbers[0] - numbers[1]
            range_length = numbers[2]
            self.ranges.append(Range(range_start, range_offset, range_length))
    
    def map(self, source):
        for range in self.ranges:
            if range.contains(source):
                return source + range.offset
        
        # No ranges matched, return original value
        return source

# map input into blocks
blocks = [[]]
current_block = blocks[0]

for line in raw_data.splitlines():
    if line != '':
        current_block.append(line)
    else: 
        current_block = []
        blocks.append(current_block)
    
# The first block is the list of seeds to be mapped
seeds_list = [int(number) for number in blocks[0][0].split()[1:]]

# The remaining blocks are range maps
range_maps = [Map(block) for block in blocks[1:]]

# Apply the maps in order to each seed
apply_map = lambda value, map: map.map(value)
locations = [reduce(apply_map, range_maps, seed) for seed in seeds_list]
print(min(locations))
