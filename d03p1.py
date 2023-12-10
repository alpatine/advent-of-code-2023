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
number_sum = 0
while row < height:
    col = 0
    while col < width:
        char = matrix[row][col]
        if char.isdigit():
            # start of a number, find the end
            stop_col = col + 1
            while stop_col < width:
                if not matrix[row][stop_col].isdigit():
                    break
                stop_col += 1
            
            # track if the number should be included
            # Can be set to True more than once to keep code simpler (even if slower)
            include_number = False
            is_symbol = lambda c: c != '.' and not c.isdigit()

            # check extant rows above and below for symbols
            rows_to_check = []
            if row > 0:
                rows_to_check.append(row-1)
            if row + 1 < height:
                rows_to_check.append(row+1)
            for check_row in rows_to_check:
                for check_col in range(max(0, col - 1), min(stop_col + 1, width)):
                    check_char = matrix[check_row][check_col]
                    if is_symbol(check_char):
                        include_number = True
                        break

            # check either end of the numebr for symbols
            cols_to_check = []
            if col > 0:
                cols_to_check.append(col - 1)
            if stop_col < width:
                cols_to_check.append(stop_col)
            for check_col in cols_to_check:
                check_char = matrix[row][check_col]
                if is_symbol(check_char):
                    include_number = True
            
            # determine the number and add to sum
            if include_number:
                number_chars = matrix[row][col:stop_col]
                number_string = ''.join(number_chars)
                number_sum += int(number_string)
            col = stop_col
        else:
            col += 1
    row += 1

print(number_sum)