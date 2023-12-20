with open('d04data.txt') as file:
    raw_data = file.read()

# raw_data = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''

class Card:
    def __init__(self, line):
        card_part, number_lists_part = line.split(':')
        self.card_number = int(card_part.split(' ')[-1].strip())
        
        winning_numbers_part, my_numbers_part = number_lists_part.split('|')
        self.winning_numbers = map(int, map(str.strip, winning_numbers_part.strip().split()))
        self.my_numbers = map(int, map(str.strip, my_numbers_part.strip().split()))
    
    def points(self):
        winning_numbers = set(self.winning_numbers)
        my_numbers = set(self.my_numbers)
        matches = winning_numbers.intersection(my_numbers)
        match_count = len(matches)
        if match_count > 0:
            return 2 ** (match_count-1)
        else: return 0

# Parse the data into a list of cards
lines = raw_data.splitlines()
cards = map(Card, lines)
print(sum(map(Card.points, cards)))