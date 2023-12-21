from math import ceil, floor, prod, sqrt

raw_data = '''Time:      7  15   30
Distance:  9  40  200'''

with open('d06data.txt') as file:
    raw_data = file.read()

def parse_races(lines):
    time_line, dist_line = lines.splitlines()
    extract_numbers = lambda line: map(int, map(str.strip, line.split(':')[1].strip().split()))
    time_numbers = extract_numbers(time_line)
    dist_numbers = extract_numbers(dist_line)
    return zip(time_numbers, dist_numbers)

def number_of_winning_holds(race):
    time,dist = race
    shortest_hold = floor((0.5 * (time - sqrt(time*time - 4*dist))) + 1)
    longest_hold = ceil((0.5 * (time + sqrt(time*time - 4*dist))) - 1)
    winning_holds = longest_hold - shortest_hold + 1
    return winning_holds

races = parse_races(raw_data)
hold_times = map(number_of_winning_holds, races)
hold_product = prod(hold_times)
print(hold_product)