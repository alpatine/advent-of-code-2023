from itertools import combinations


def expand_grid(grid: list[list[str]], empty_rows: list[int], empty_cols:list[int]):
    grid_width = len(grid[0])

    empty_rows.sort(reverse=True)
    empty_cols.sort(reverse=True)

    # Add empty rows
    for empty_row in empty_rows:
        grid.insert(empty_row, ['.'] * grid_width)
    
    # Add empty cols
    for row in grid:
        for empty_col in empty_cols:
            row.insert(empty_col, '.')
    
    return grid

def find_expansions(grid):
    rows_with_galaxies = []
    cols_with_galaxies = []
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if col == '#':
                rows_with_galaxies.append(row_index)
                cols_with_galaxies.append(col_index)

    empty_rows = list(set(range(0, len(grid))).difference(rows_with_galaxies))
    empty_cols = list(set(range(0, len(grid[0]))).difference(cols_with_galaxies))

    return (empty_rows, empty_cols)

def find_galaxies(grid):
    galaxies = []
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if col == '#':
                galaxies.append((row_index, col_index))
    return galaxies

def parse_input(data: str) -> list[list[str]]:
    grid = [list(s) for s in data.splitlines()]
    return grid

def d11p1(data = None):
    if data is None:
        with open('d11data.txt') as file:
            data = file.read()

    grid = parse_input(data)
    empty_rows, empty_cols = find_expansions(grid)
    grid = expand_grid(grid, empty_rows, empty_cols)
    galaxies = find_galaxies(grid)

    distance_sum = 0
    for left,right in combinations(galaxies, 2):
        distance = abs(right[0] - left[0]) + abs(right[1] - left[1])
        distance_sum += distance
    
    return distance_sum

if __name__ == '__main__':
    print(d11p1())
