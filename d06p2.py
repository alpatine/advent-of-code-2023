from math import ceil, floor, sqrt

raw_data = '''Time:      7  15   30
Distance:  9  40  200'''

with open('d06data.txt') as file:
    raw_data = file.read()

def parse_race(lines):
    time_line, dist_line = lines.splitlines()
    condense_numbers = lambda line: int(''.join(map(str.strip, line.split(':')[1].strip().split())))
    time = condense_numbers(time_line)
    dist = condense_numbers(dist_line)
    return (time, dist)

def number_of_winning_holds(race):
    time,dist = race
    shortest_hold = floor((0.5 * (time - sqrt(time*time - 4*dist))) + 1)
    longest_hold = ceil((0.5 * (time + sqrt(time*time - 4*dist))) - 1)
    winning_holds = longest_hold - shortest_hold + 1
    return winning_holds

race = parse_race(raw_data)
winning_holds = number_of_winning_holds(race)
print(winning_holds)
