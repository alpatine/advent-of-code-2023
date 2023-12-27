from math import prod


def extract_number(grid, row, col):
    width = len(grid[0])
    start_col = col
    stop_col = start_col + 1
    while start_col >= 0 and grid[row][start_col - 1].isdigit():
        start_col -= 1
    while stop_col < width and grid[row][stop_col].isdigit():
        stop_col += 1
    return int(''.join(grid[row][start_col:stop_col]))

def d03p2(raw_data = None):
    if raw_data is None:
        with open('d03data.txt') as file:
            raw_data = file.read()
    # convert the block of text into a character grid
    grid = [[char for char in line] for line in raw_data.splitlines()]
    height = len(grid)
    width = len(grid[0])

    row = 0
    gear_ratio_sum = 0
    while row < height:
        col = 0
        while col < width:
            char = grid[row][col]
            if char == '*':
                gear_ratio_factors = []
                # Could be a gear - need to detect numbers around it

                # check if there is a number to the left
                if col > 0 and grid[row][col - 1].isdigit():
                    gear_ratio_factors.append(extract_number(grid, row, col - 1))
                
                # check if there is a number to the right
                if col + 1 < width and grid[row][col + 1].isdigit():
                    gear_ratio_factors.append(extract_number(grid, row, col + 1))
                
                # check for numbers above and below
                rows_to_check = []
                if row > 0:
                    rows_to_check.append(row - 1)
                if row + 1 < height:
                    rows_to_check.append(row + 1)
                for check_row in rows_to_check:
                    if grid[check_row][col].isdigit():
                        # if the char directly above/below is a digit, there can only be one number
                        gear_ratio_factors.append(extract_number(grid, check_row, col))
                    else:
                        # need to check to the left and right on the row, could be two numbers
                        if col > 0 and grid[check_row][col - 1].isdigit():
                            gear_ratio_factors.append(extract_number(grid, check_row, col - 1))
                        
                        if col + 1 < width and grid[check_row][col + 1].isdigit():
                            gear_ratio_factors.append(extract_number(grid, check_row, col + 1))

                if len(gear_ratio_factors) == 2:
                    gear_ratio = prod(gear_ratio_factors)
                    gear_ratio_sum += gear_ratio

            col += 1
        row += 1

    return gear_ratio_sum

if __name__ == '__main__':
    print(d03p2())
