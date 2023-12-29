class Mapper:
    EAST = 0
    NORTH = 1
    WEST = 2
    SOUTH = 3

    def __init__(self,
                 grid: list[list[str]],
                 start_position: tuple[int, int]) -> None:
        self.grid = grid
        self.map = [['.' for col in row] for row in grid]
        self.start = start_position
        self.position = start_position
        self.last_direction = None
        self.steps = 0
        self.inside_count = 0
    
    def next_direction(self):
        node = self.grid[self.position[0]][self.position[1]]
        match (node, self.last_direction):
            case ('|', _): return self.last_direction
            case ('-', _): return self.last_direction
            case ('L', Mapper.SOUTH): return Mapper.EAST
            case ('L', Mapper.WEST): return Mapper.NORTH
            case ('J', Mapper.EAST): return Mapper.NORTH
            case ('J', Mapper.SOUTH): return Mapper.WEST
            case ('7', Mapper.EAST): return Mapper.SOUTH
            case ('7', Mapper.NORTH): return Mapper.WEST
            case ('F', Mapper.WEST): return Mapper.SOUTH
            case ('F', Mapper.NORTH): return Mapper.EAST
            case ('.', _): return None
            case ('S', _):
                right_node = self.grid[self.position[0]][self.position[1]+1]
                if right_node in ['-', 'J', '7']: return Mapper.EAST
                up_node = self.grid[self.position[0]-1][self.position[1]]
                if up_node in ['|', '7', 'F']: return Mapper.NORTH
                left_node = self.grid[self.position[0]][self.position[1]-1]
                if left_node in ['-', 'L', 'F']: return Mapper.WEST
    
    def step(self, direction):
        self.steps += 1
        self.last_direction = direction
        match direction:
            case Mapper.EAST: self.position = (self.position[0], self.position[1]+1)
            case Mapper.NORTH: self.position = (self.position[0]-1, self.position[1])
            case Mapper.WEST: self.position = (self.position[0], self.position[1]-1)
            case Mapper.SOUTH: self.position = (self.position[0]+1, self.position[1])

    def map_loop(self):
        while True:
            direction = self.next_direction()
            self.step(direction)
            self.map[self.position[0]][self.position[1]] = 'L'
            if self.position == self.start:
                break
    
    def find_inside(self):
        for row_index, row in enumerate(self.grid):
            inside_loop = False
            up_entry = False
            down_entry = False
            for col_index, col in enumerate(row):
                map_node = self.map[row_index][col_index]
                if map_node == 'L':
                    # node is on the loop, check if vertical
                    grid_node = self.grid[row_index][col_index]
                    match grid_node:
                        case '|': inside_loop = not inside_loop
                        case 'L': up_entry = True
                        case 'J':
                            if down_entry: inside_loop = not inside_loop
                            up_entry = down_entry = False
                        case 'F': down_entry = True
                        case '7':
                            if up_entry: inside_loop = not inside_loop
                            up_entry = down_entry = False
                else:
                    if inside_loop:
                        # Inside the loop
                        self.map[row_index][col_index] = 'I'
                        self.inside_count += 1
                    else:
                        self.map[row_index][col_index] = 'O'

def parse_input(raw_data: str) -> list[list[str]]:
    grid = [list(s) for s in raw_data.splitlines()]
    return grid

def locate_start(grid: list[list[str]]) -> tuple[int, int]:
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if col == 'S':
                return (row_index, col_index)
    return None

def d10p2(raw_data = None):
    if raw_data is None:
        with open('d10data.txt') as file:
            raw_data = file.read()
    
    grid = parse_input(raw_data)
    start = locate_start(grid)
    mapper = Mapper(grid, start)
    mapper.map_loop()
    mapper.find_inside()
    return mapper.inside_count

if __name__ == '__main__':
    print(d10p2())
