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

with open('d02data.txt') as file:
    raw_data = file.read()

# raw_data = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

games = [parse_line(line) for line in raw_data.splitlines()]

limits = [12, 13, 14]
game_id_sum = 0
for game in games:
    valid_game = True
    for draw in game[1]:
        for color_index in range(3):
            if draw[color_index] > limits[color_index]:
                valid_game = False
    if valid_game:
        game_id_sum += game[0]
print(game_id_sum)
