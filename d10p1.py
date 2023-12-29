class Walker:
    EAST = 0
    NORTH = 1
    WEST = 2
    SOUTH = 3

    def __init__(self,
                 grid: list[list[str]],
                 start_position: tuple[int, int]) -> None:
        self.grid = grid
        self.start = start_position
        self.position = start_position
        self.last_direction = None
        self.steps = 0
    
    def next_direction(self):
        node = self.grid[self.position[0]][self.position[1]]
        match (node, self.last_direction):
            case ('|', _): return self.last_direction
            case ('-', _): return self.last_direction
            case ('L', Walker.SOUTH): return Walker.EAST
            case ('L', Walker.WEST): return Walker.NORTH
            case ('J', Walker.EAST): return Walker.NORTH
            case ('J', Walker.SOUTH): return Walker.WEST
            case ('7', Walker.EAST): return Walker.SOUTH
            case ('7', Walker.NORTH): return Walker.WEST
            case ('F', Walker.WEST): return Walker.SOUTH
            case ('F', Walker.NORTH): return Walker.EAST
            case ('.', _): return None
            case ('S', _):
                right_node = self.grid[self.position[0]][self.position[1]+1]
                if right_node in ['-', 'J', '7']: return Walker.EAST
                up_node = self.grid[self.position[0]-1][self.position[1]]
                if up_node in ['|', '7', 'F']: return Walker.NORTH
                left_node = self.grid[self.position[0]][self.position[1]-1]
                if left_node in ['-', 'L', 'F']: return Walker.WEST
    
    def step(self, direction):
        self.steps += 1
        self.last_direction = direction
        match direction:
            case Walker.EAST: self.position = (self.position[0], self.position[1]+1)
            case Walker.NORTH: self.position = (self.position[0]-1, self.position[1])
            case Walker.WEST: self.position = (self.position[0], self.position[1]-1)
            case Walker.SOUTH: self.position = (self.position[0]+1, self.position[1])

    def walk_loop(self):
        while True:
            direction = self.next_direction()
            self.step(direction)
            if self.position == self.start:
                break

def parse_input(raw_data: str) -> list[list[str]]:
    grid = [list(s) for s in raw_data.splitlines()]
    return grid

def locate_start(grid: list[list[str]]) -> tuple[int, int]:
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if col == 'S':
                return (row_index, col_index)
    return None

def d10p1(raw_data = None):
    if raw_data is None:
        with open('d10data.txt') as file:
            raw_data = file.read()
    
    grid = parse_input(raw_data)
    start = locate_start(grid)
    walker = Walker(grid, start)
    walker.walk_loop()
    return walker.steps // 2

if __name__ == '__main__':
    print(d10p1())
