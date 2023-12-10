from math import prod


raw_data = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''

with open('d03data.txt') as file:
    raw_data = file.read()

# convert the block of text into a character matrix
matrix = [[char for char in line] for line in raw_data.splitlines()]
height = len(matrix)
width = len(matrix[0])

row = 0
gear_ratio_sum = 0
while row < height:
    col = 0
    while col < width:
        char = matrix[row][col]
        if char == '*':
            gear_ratio_factors = []
            # Could be a gear - need to detect numbers around it

            # check if there is a number to the left
            if col > 0 and matrix[row][col - 1].isdigit():
                start_col = col - 1
                stop_col = start_col + 1
                while start_col >= 0 and matrix[row][start_col - 1].isdigit():
                    start_col -= 1
                factor = int(''.join(matrix[row][start_col:stop_col]))
                gear_ratio_factors.append(factor)
            
            # check if there is a number to the right
            if col + 1 < width and matrix[row][col + 1].isdigit():
                start_col = col + 1
                stop_col = start_col + 1
                while stop_col < width and matrix[row][stop_col].isdigit():
                    stop_col += 1
                factor = int(''.join(matrix[row][start_col:stop_col]))
                gear_ratio_factors.append(factor)
            
            # check for numbers above and below
            rows_to_check = []
            if row > 0:
                rows_to_check.append(row - 1)
            if row + 1 < height:
                rows_to_check.append(row + 1)
            for check_row in rows_to_check:
                if matrix[check_row][col].isdigit():
                    # if the char directly above/below id a digit, there can only be one number
                    start_col = col
                    stop_col = col + 1
                    # determine how far left this goes
                    while start_col >= 0 and matrix[check_row][start_col - 1].isdigit():
                        start_col -= 1
                    while stop_col < width and matrix[check_row][stop_col].isdigit():
                        stop_col += 1
                    factor = int(''.join(matrix[check_row][start_col:stop_col]))
                    gear_ratio_factors.append(factor)
                else:
                    # need to check to the left and right on the row, could be two numbers
                    if col > 0 and matrix[check_row][col - 1].isdigit():
                        start_col = col - 1
                        stop_col = start_col + 1
                        while start_col >= 0 and matrix[check_row][start_col - 1].isdigit():
                            start_col -= 1
                        factor = int(''.join(matrix[check_row][start_col:stop_col]))
                        gear_ratio_factors.append(factor)
                    
                    if col + 1 < width and matrix[check_row][col + 1].isdigit():
                        start_col = col + 1
                        stop_col = start_col + 1
                        while stop_col < width and matrix[check_row][stop_col].isdigit():
                            stop_col += 1
                        factor = int(''.join(matrix[check_row][start_col:stop_col]))
                        gear_ratio_factors.append(factor)

            if len(gear_ratio_factors) == 2:
                gear_ratio = prod(gear_ratio_factors)
                gear_ratio_sum += gear_ratio

        col += 1
    row += 1

print(gear_ratio_sum)