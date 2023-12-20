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
        self.winning_numbers = [int(number) for number in [number_part.strip() for number_part in winning_numbers_part.strip().split()]]
        self.my_numbers = [int(number) for number in [number_part.strip() for number_part in my_numbers_part.strip().split()]]
    
    def cards_won(self):
        winning_numbers = set(self.winning_numbers)
        my_numbers = set(self.my_numbers)
        matches = winning_numbers.intersection(my_numbers)
        return len(matches)

lines = raw_data.splitlines()
cards = list(map(Card, lines))
card_counts = [1] * len(cards)

for card_index in range(len(cards)-1, -1, -1):
    card = cards[card_index]
    cards_won = card.cards_won()
    for won_index in range(card_index + 1, card_index + 1 + cards_won):
        card_counts[card_index] += card_counts[won_index]

print(sum(card_counts))
