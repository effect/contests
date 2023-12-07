# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

result = 0
for line in lines:
	line = line.split(':')[-1].strip()
	wins, nums = line.split('|')
	wins = set([int(a) for a in wins.strip().split()])
	nums = [int(a) for a in nums.strip().split()]
	cnt_win = 0
	for num in nums:
		if num in wins:
			cnt_win += 1
	if cnt_win > 0:
		result += 2 ** (cnt_win - 1)
print(result)

