from math import ceil, floor, sqrt


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

def d06p2(raw_data = None):
    if raw_data is None:
        with open('d06data.txt') as file:
            raw_data = file.read()
    race = parse_race(raw_data)
    winning_holds = number_of_winning_holds(race)
    return winning_holds

if __name__ == '__main__':
    print(d06p2())
