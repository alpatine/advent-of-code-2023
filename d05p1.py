from functools import reduce

from parsing import split_data_into_blocks


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

def d05p1(raw_data = None):
    if raw_data is None:
        with open('d05data.txt') as file:
            raw_data = file.read()

    # map input into blocks
    blocks = split_data_into_blocks(raw_data)
        
    # The first block is the list of seeds to be mapped
    seeds_list = [int(number) for number in blocks[0][0].split()[1:]]

    # The remaining blocks are range maps
    range_maps = [Map(block) for block in blocks[1:]]

    # Apply the maps in order to each seed
    apply_map = lambda value, map: map.map(value)
    locations = [reduce(apply_map, range_maps, seed) for seed in seeds_list]
    return min(locations)

if __name__ == '__main__':
    print(d05p1())
