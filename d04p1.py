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

def d04p1(raw_data = None):
    if raw_data is None:
        with open('d04data.txt') as file:
            raw_data = file.read()
    # Parse the data into a list of cards
    lines = raw_data.splitlines()
    cards = map(Card, lines)
    return sum(map(Card.points, cards))

if __name__ == '__main__':
    print(d04p1())
