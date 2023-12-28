from itertools import cycle

from parsing import split_data_into_blocks

START_ELEMENT = 'AAA'
END_ELEMENT = 'ZZZ'

def parse_line(line: str):
    start_part, turn_part = line.split('=')
    start = start_part.strip()

    turn_part = turn_part.strip()
    left,right = list(map(str.strip, turn_part[1:-1].split(',')))
    return (start, left, right)

def d08p1(raw_data = None):
    if raw_data is None:
        with open('d08data.txt') as file:
            raw_data = file.read()
    blocks = split_data_into_blocks(raw_data)
    instructions = cycle(map(int, blocks[0][0].replace('L','0').replace('R','1')))   
    network = {start: (left, right) for start, left, right in map(parse_line, blocks[1])}

    steps = 0
    current_node = START_ELEMENT
    while current_node != END_ELEMENT:
        steps += 1
        direction = next(instructions)
        current_node = network[current_node][direction]
    
    return steps
    
if __name__ == '__main__':
    print(d08p1())
