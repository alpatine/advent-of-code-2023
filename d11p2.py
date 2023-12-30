from itertools import combinations


def find_expansions(grid):
    rows_with_galaxies = []
    cols_with_galaxies = []
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if col == '#':
                rows_with_galaxies.append(row_index)
                cols_with_galaxies.append(col_index)

    empty_rows = set(range(0, len(grid))).difference(rows_with_galaxies)
    empty_cols = set(range(0, len(grid[0]))).difference(cols_with_galaxies)

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

def d11p2(expansion_size, data = None):
    if data is None:
        with open('d11data.txt') as file:
            data = file.read()
    
    grid = parse_input(data)
    empty_rows, empty_cols = find_expansions(grid)
    galaxies = find_galaxies(grid)

    distance_sum = 0
    for left, right in combinations(galaxies, 2):
        row_min = min(left[0], right[0])
        row_max = max(left[0], right[0])
        col_min = min(left[1], right[1])
        col_max = max(left[1], right[1])

        expanded_rows = set(range(row_min, row_max)).intersection(empty_rows)
        expanded_cols = set(range(col_min, col_max)).intersection(empty_cols)
        row_distance = row_max - row_min + (expansion_size-1) * len(expanded_rows)
        col_distance = col_max - col_min + (expansion_size-1) * len(expanded_cols)
        distance_sum += row_distance + col_distance
    
    return distance_sum

if __name__ == '__main__':
    print(d11p2(1000000))
