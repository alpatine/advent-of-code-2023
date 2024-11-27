def count_arrangements(spring_row: str,
                       damaged_groups: list[int],
                       cache: dict[tuple[str, tuple[int]], int] = {}
                       )-> int:
    
    # Prepare data and calc key metrics
    # Remove any leading '.', no blocks can go there.
    spring_row = spring_row.lstrip('.')
    spring_row_len = len(spring_row)
    damaged_groups_count = len(damaged_groups)
    damaged_groups_min_space = sum(damaged_groups) + damaged_groups_count - 1
    number_of_arrangements = 0
    key = (spring_row, tuple(damaged_groups))

    # Check base cases
    if key in cache: return cache[key]
    if spring_row_len < damaged_groups_min_space:
        cache[key] = 0
        return 0
    
    match spring_row_len, damaged_groups_count:
        # empty string with no more groups
        case 0, 0:
            cache[key] = 1
            return 1 

        # empty string with groups to be placed
        case 0, _:
            cache[key] = 0
            return 0 

        # non-empty string and no more groups can be placed
        case _, 0:
            if '#' in spring_row:
                cache[key] = 0
                return 0
            else:
                cache[key] = 1
                return 1

    # First branch - remove the first char
    if spring_row.startswith('#') == False:
        remaining_spring_row = spring_row[1:]
        number_of_arrangements += count_arrangements(remaining_spring_row, damaged_groups, cache)

    # Second branch - use the first group
    # make sure there are no '.' within the group nor a '#' right after it.
    # If this is not the last group we need to take one additional space.
    group = damaged_groups[0]
    if not '.' in spring_row[:group]:
        remaining_spring_row = spring_row[group:]
        if not remaining_spring_row.startswith('#'):
            if damaged_groups_count > 1:
                remaining_spring_row = remaining_spring_row[1:]
            remaining_groups = damaged_groups[1:]
            number_of_arrangements += count_arrangements(remaining_spring_row, remaining_groups, cache)

    # Both branches checked, return what we found
    cache[key] = number_of_arrangements
    return number_of_arrangements


def parse_input(data: str) -> list[tuple[str,list[int]]]:
    springs = []
    lines = data.splitlines()
    for line in lines:
        spring_row, damaged_group_part = line.split(' ')
        damaged_groups = list(map(int, damaged_group_part.split(',')))
        springs.append((spring_row, damaged_groups))
    return springs


def d12p1(data = None):
    if data is None:
        with open('d12data.txt') as file:
            data = file.read()
    
    number_of_arrangements = 0
    spring_conditions = parse_input(data)
    for spring_condition in spring_conditions:
        condition_arrangements = count_arrangements(*spring_condition)
        #print(f'{spring_condition[0]} {spring_condition[1]} -> {condition_arrangements}')
        number_of_arrangements += condition_arrangements

    return number_of_arrangements


if __name__ == '__main__':
    print(d12p1())
