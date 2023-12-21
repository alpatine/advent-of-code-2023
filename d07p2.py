from collections import Counter

raw_data = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''

with open('d07data.txt') as file:
    raw_data = file.read()

class Hand:
    # Hand Types
    FIVE_KIND = 7
    FOUR_KIND = 6
    FULL_HOUSE = 5
    THREE_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1

    rank_values = {rank: value for rank,value in zip(
        ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A'], 
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])}

    def __init__(self, line) -> None:
        self.cards, bid_str = line.split()
        self.card_values = list(map(self.rank_values.get, self.cards))
        self.bid = int(bid_str)

        # Count each card rank
        card_counts = Counter(self.cards)
        
        # Handle jokers
        joker_count = card_counts['J']
        if joker_count > 0:
            if joker_count == 5:
                # All Jokers - make them aces!
                card_counts['A'] = 5
                del card_counts['J']
            else:
                # Replace jokers with most common card (that's not a joker)
                ordered_card_counts = card_counts.most_common()
                if ordered_card_counts[0][0] != 'J':
                    most_common_card = ordered_card_counts[0][0]
                else:
                    most_common_card = ordered_card_counts[1][0]
                card_counts[most_common_card] += joker_count
                del card_counts['J']
        
        # Determine hand types
        ordered_card_counts = card_counts.most_common()
        distinct_cards = len(ordered_card_counts)
        high_count = ordered_card_counts[0][1]
        match(distinct_cards, high_count):
            case (1,_): self.type = Hand.FIVE_KIND
            case (2,4): self.type = Hand.FOUR_KIND
            case (2,3): self.type = Hand.FULL_HOUSE
            case (3,3): self.type = Hand.THREE_KIND
            case (3,2): self.type = Hand.TWO_PAIR
            case (4,_): self.type = Hand.ONE_PAIR
            case _: self.type = Hand.HIGH_CARD
    
    def __lt__(self, other):
        return (self.type, *self.card_values) < (other.type, *other.card_values)
    
    def __repr__(self) -> str:
        return self.cards


hands = [Hand(line) for line in raw_data.splitlines()]
hands.sort()

print(sum(hand.bid * rank for hand,rank in zip(hands, range(1, len(hands)+1))))
