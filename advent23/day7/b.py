from collections import Counter
f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3',  '2', 'J']
cards = [0] * len(lines)
nums = [0] * len(lines)
for i, line in enumerate(lines):
	cards[i], nums[i] = line.split()
	nums[i] = int(nums[i].strip())
# print(cards)
# print(nums)


def comparator_for_one_type(type_cnt):
	_, cnt = type_cnt
	return cnt


def get_max_non_j(cards):
	cards_cnt = Counter(cards)
	cards_cnt = sorted(cards_cnt.items(), key=comparator_for_one_type, reverse=True)
	for card_cnt in cards_cnt:
		card = card_cnt[0]
		if card != 'J':
			return card
	return 'J'


def comparator(cur_cards):
	cur_cards = cur_cards[0]
	no_joker_cards = cur_cards
	if 'J' in cur_cards:
		no_joker_cards = cur_cards.replace('J', get_max_non_j(cur_cards))
	cards_cnt = Counter(no_joker_cards)		
	combination = None
	if 5 in cards_cnt.values():
		combination = 10
	elif 4 in cards_cnt.values():
		combination = 8
	elif 3 in cards_cnt.values() and 2 in cards_cnt.values():
		combination = 7
	elif 3 in cards_cnt.values():
		combination = 6
	elif list(cards_cnt.values()).count(2) == 2:
		combination = 5
	elif 2 in cards_cnt.values():
		combination = 4
	else:
		combination = 2
	return (combination, *(len(order) - order.index(c) for c in cur_cards) )


pairs = list(zip(cards, nums))
sorted_cards = sorted(pairs, key=comparator)
sorted_cards, nums = zip(*sorted_cards)
print(sorted_cards)
# print(nums)
result = 0
for i in range(len(lines)):
	result += (i + 1) * nums[i]
print(result)