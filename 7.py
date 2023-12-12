from collections import Counter

testinput = "32T3K 765\nT55J5 684\nKK677 28\nKTJJT 220\nQQQJA 483"
testdata = testinput.split("\n")

file = open('7-input.txt')
lines = file.readlines()

hands = []

for line in lines:
    line = line.replace("\n", "")
    hands.append(line)

def card_rank_value(card):
    """ Returns the numerical value of a card's rank. """
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10,
              'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return values[card]

def hand_rank_with_original_order_tiebreaker(hand):
    """ Return a value indicating the ranking of a hand, with a tiebreaker based on the original order of cards. """
    cards = hand.split(" ")[0]
    original_order_ranks = [card_rank_value(card) for card in cards]
    sorted_ranks = sorted(original_order_ranks, reverse=True)
    counts = Counter(sorted_ranks)
    sorted_counts = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)

    if sorted_counts[0][1] == 5:
        return (6, sorted_counts[0][0], original_order_ranks)  # Five of a Kind
    elif sorted_counts[0][1] == 4:
        return (5, sorted_counts[0][0], original_order_ranks)  # Four of a Kind
    elif sorted_counts[0][1] == 3 and sorted_counts[1][1] == 2:
        return (4, sorted_counts[0][0], original_order_ranks)  # Full House
    elif sorted_counts[0][1] == 3:
        return (3, sorted_counts[0][0], original_order_ranks)  # Three of a Kind
    elif sorted_counts[0][1] == 2 and sorted_counts[1][1] == 2:
        return (2, sorted_counts[0][0], original_order_ranks)  # Two Pair
    elif sorted_counts[0][1] == 2:
        return (1, sorted_counts[0][0], original_order_ranks)  # One Pair
    return (0, original_order_ranks[0], original_order_ranks)  # High Card

def sort_poker_hands_with_original_order_tiebreaker(combinations):
    """ Sorts an array of card combinations with a tiebreaker based on the original order of cards. """
    return sorted(combinations, key=hand_rank_with_original_order_tiebreaker, reverse=False)

sorted_combinations = sort_poker_hands_with_original_order_tiebreaker(hands)

print(sorted_combinations)

winnings = 0

for index, hand in enumerate(sorted_combinations):
    bid = hand.split(" ")[1]
    winnings += (index + 1) * int(bid)
    
print(winnings)

# 245898409 too low
    