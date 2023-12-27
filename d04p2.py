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

def d04p2(raw_data = None):
    if raw_data is None:
        with open('d04data.txt') as file:
            raw_data = file.read()

    lines = raw_data.splitlines()
    cards = list(map(Card, lines))
    card_counts = [1] * len(cards)

    for card_index in range(len(cards)-1, -1, -1):
        card = cards[card_index]
        cards_won = card.cards_won()
        for won_index in range(card_index + 1, card_index + 1 + cards_won):
            card_counts[card_index] += card_counts[won_index]

    return sum(card_counts)

if __name__ == '__main__':
    print(d04p2())
