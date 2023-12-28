from itertools import cycle
from math import lcm

from parsing import split_data_into_blocks


def parse_line(line: str):
    start_part, turn_part = line.split('=')
    start = start_part.strip()

    turn_part = turn_part.strip()
    left,right = list(map(str.strip, turn_part[1:-1].split(',')))
    return (start, left, right)

def is_end_node(node):
    return node.endswith('Z')

def prepare_instructions(instruction_string):
    return cycle(map(int, instruction_string.replace('L','0').replace('R','1')))

def d08p2(raw_data = None):
    if raw_data is None:
        with open('d08data.txt') as file:
            raw_data = file.read()
    
    blocks = split_data_into_blocks(raw_data)
    instruction_str = blocks[0][0]
    network = {start: (left, right) for start, left, right in map(parse_line, blocks[1])}
    start_nodes = [node for node in network.keys() if node.endswith('A')]
    
    loop_lengths = []
    for position in start_nodes:
        steps = 0
        instructions = prepare_instructions(instruction_str)
        while not is_end_node(position):
            steps += 1
            direction = next(instructions)
            position = network[position][direction]
        loop_lengths.append(steps)
    return lcm(*loop_lengths)
    
if __name__ == '__main__':
    print(d08p2())
