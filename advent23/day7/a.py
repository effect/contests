from collections import Counter
f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3',  '2']
cards = [0] * len(lines)
nums = [0] * len(lines)
for i, line in enumerate(lines):
	cards[i], nums[i] = line.split()
	nums[i] = int(nums[i].strip())
print(cards)
print(nums)


def comparator(cur_cards):
	cur_cards = cur_cards[0]
	cards_cnt = Counter(cur_cards)
	combination = None
	if 5 in cards_cnt.values():
		combination = 5
	elif 4 in cards_cnt.values():
		combination = 4
	elif 3 in cards_cnt.values() and 2 in cards_cnt.values():
		combination = 3.5
	elif 3 in cards_cnt.values():
		combination = 3
	elif list(cards_cnt.values()).count(2) == 2:
		combination = 2.5
	elif 2 in cards_cnt.values():
		combination = 2
	else:
		combination = 1
	return (combination, *(len(order) - order.index(c) for c in cur_cards) )


pairs = list(zip(cards, nums))
sorted_cards = sorted(pairs, key=comparator)
sorted_cards, nums = zip(*sorted_cards)
print(sorted_cards)
print(nums)
result = 0
for i in range(len(lines)):
	result += (i + 1) * nums[i]
print(result)