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

def calculate_valibration_value(line):
    first_digit = find_substring(line, number_strings, False)
    last_digit = find_substring(line, number_strings, True)
    calibration_value = int(first_digit + last_digit)
    return calibration_value

def d01p1(raw_data = None):
    if raw_data is None:
        with open('d01data.txt') as file:
            raw_data = file.read()
    lines = raw_data.splitlines()
    calibration_values = map(calculate_valibration_value, lines)
    calibration_value_sum = sum(calibration_values)
    return calibration_value_sum

if __name__ == '__main__':
    result = d01p1()
    print(result)