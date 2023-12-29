from itertools import pairwise


def predict_next_value(sequence):
    def is_zero(n): return n == 0
    stack = []
    while not all(map(is_zero, sequence)):
        stack.append(sequence)
        new_sequence = []
        for left,right in pairwise(sequence):
            new_sequence.append(right - left)
        sequence = new_sequence
    
    total = 0
    for sequence in reversed(stack):
        total = sequence[0] - total
    return total

def d09p2(raw_data = None):
    if raw_data is None:
        with open('d09data.txt') as file:
            raw_data = file.read()
    
    next_value_sum = 0
    for line in raw_data.splitlines():
        sequence = [int(s) for s in line.split()]
        next_value = predict_next_value(sequence)
        next_value_sum += next_value

    return next_value_sum

if __name__ == '__main__':
    print(d09p2())
