# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]
add = [0] * len(lines)

result = len(lines)
for index in range(len(lines) - 1, -1, -1):
	line = lines[index]
	line = line.split(':')[-1].strip()
	wins, nums = line.split('|')
	wins = set([int(a) for a in wins.strip().split()])
	nums = [int(a) for a in nums.strip().split()]
	cnt_win = 0
	for num in nums:
		if num in wins:
			cnt_win += 1
	if cnt_win > 0:
		add[index] += cnt_win
		for i in range(cnt_win):
			add[index] += add[index + i + 1]
	result += add[index]
	# print(index, add)
print(result)

