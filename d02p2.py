from math import prod


def parse_line(line:str) -> tuple[int, list[tuple[int, int, int]]]:
    colour_parts_map = {'red': 0, 'green': 1, 'blue': 2}
    game_part, draws_part = line.split(':')
    game_id = int(game_part.strip().replace('Game ', ''))
    draw_texts = draws_part.split(';')
    draws = []
    for draw_text in draw_texts:
        colour_values = [0, 0, 0]
        colour_parts = draw_text.split(',')
        for colour_part in colour_parts:
            colour_part = colour_part.strip()
            count, colour = colour_part.split(' ')
            colour = colour.strip()
            colour_values[colour_parts_map[colour]] = int(count)
        draws.append(colour_values)
    return (game_id, draws)

def d02p2(raw_data = None):
    if raw_data is None:
        with open('d02data.txt') as file:
            raw_data = file.read()

    games = [parse_line(line) for line in raw_data.splitlines()]

    game_power_sum = 0
    for game in games:
        max_colour_count = [0, 0, 0]
        for draw in game[1]:
            for color_index in range(3):
                max_colour_count[color_index] = max(max_colour_count[color_index], draw[color_index])
        game_power_sum += prod(max_colour_count)
    return game_power_sum

if __name__ == '__main__':
    print(d02p2())
