data = open('inputs/day7_input.txt', 'r').read().split('\n')
hands_and_bids = dict()
for line in data:
    helper = [x for x in line.split(" ")]    
    hands_and_bids[helper[0]] = int(helper[1])

def hand_to_dict(hand):
    helper = dict()
    for char in hand:
        if char not in helper:
            helper[char] = 1
        else:
            helper[char] += 1
    return helper

def map_to_category(hand):
    counted_chars = sorted(hand_to_dict(hand).values())
    if counted_chars == [5]:
        return 1
    if counted_chars == [1, 4]:
        return 2
    if counted_chars == [2, 3]:
        return 3
    if counted_chars == [1, 1, 3]:
        return 4
    if counted_chars == [1, 2, 2]:
        return 5
    if counted_chars == [1, 1, 1, 2]:
        return 6
    else:
        return 7
    
def cards_as_int(hand: str) -> tuple:
    ordered_labels = 'AKQJT98765432'
    return (ordered_labels.index(card) for card in hand)

sorted_hands = []
for hand in hands_and_bids.keys():
    encoded_hand = (map_to_category(hand), *cards_as_int(hand), hands_and_bids[hand])
    sorted_hands.append(encoded_hand)

sorted_hands.sort(reverse=True)

output_one = 0
for i in range(1, len(sorted_hands) + 1):
    output_one += sorted_hands[i-1][-1] * i
print(output_one)

# part two

def map_to_category_with_jokers(hand):
    jokers = hand.count('J')
    fixed_hand = [c for c in hand if c != 'J']
    counted_chars = sorted(hand_to_dict(fixed_hand).values())
    if not counted_chars:
        counted_chars = [0] 
    if counted_chars[-1] + jokers == 5:
        return 1
    if counted_chars[-1] + jokers == 4:
        return 2
    if counted_chars[-1] + jokers == 3 and counted_chars[-2] == 2:
        return 3
    if counted_chars[-1] + jokers == 3:
        return 4
    if counted_chars[-1] == 2 and (jokers or counted_chars[-2] == 2):
        return 5
    if counted_chars[-1] == 2 or jokers:
        return 6
    else:
        return 7
    
def cards_as_int_with_jokers(hand: str) -> tuple:
    ordered_labels = 'AKQT98765432J'
    return (ordered_labels.index(card) for card in hand)

sorted_hands_with_jokers = []
for hand in hands_and_bids.keys():
    encoded_hand = (map_to_category_with_jokers(hand), *cards_as_int_with_jokers(hand), hands_and_bids[hand])
    sorted_hands_with_jokers.append(encoded_hand)

sorted_hands_with_jokers.sort(reverse=True)

output_two = 0
for i in range(1, len(sorted_hands_with_jokers) + 1):
    output_two += sorted_hands_with_jokers[i-1][-1] * i
print(output_two)