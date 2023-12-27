def find_substring(string, substrings, find_last):
    if find_last == False:
        # Looking for first found
        find_func = string.find
    else:
        # Looking for last found
        find_func = string.rfind
    
    sub_positions = zip(map(find_func, substrings), substrings)
    filtered_positions = (pos for pos in sub_positions if pos[0] != -1)
    ordered_positions = sorted(filtered_positions, reverse=find_last)
    if len(ordered_positions) > 0:
        return ordered_positions[0][1]
    else:
        return None

number_strings = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
number_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digit_strings = number_strings + number_words
digit_map = dict(zip(number_words, number_strings))
digit_map.update(zip(number_strings, number_strings))

def calculate_valibration_value(line):
    first_substring = find_substring(line, digit_strings, False)
    first_digit = digit_map[first_substring]

    last_substring = find_substring(line, digit_strings, True)
    last_digit = digit_map[last_substring]

    calibration_value = int(first_digit + last_digit)
    return calibration_value

def d01p2(raw_data = None):
    if raw_data is None:
        with open('d01data.txt') as file:
            raw_data = file.read()
    lines = raw_data.splitlines()
    calibration_values = map(calculate_valibration_value, lines)
    calibration_sum = sum(calibration_values)
    return calibration_sum

if __name__ == '__main__':
    result = d01p2()
    print(result)
