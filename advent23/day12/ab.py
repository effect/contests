f = open("test.in")
f = open("input.txt")


def solve(mask, cnts):
	print(mask, cnts)
	d = [[0] * len(cnts) for _ in range(len(mask))]
	# d[i][j] - number of combinations to place cnts[0..j]
	# such that cnts[j] ends exactly at index (i-1)
	# followed by space at index i
	for i in range(len(mask)):
		for j in range(len(cnts)):
			# check that we can place cnts[j] to end of mask[:i]
			if mask[i] == '#' or i - cnts[j] - 1 < 0 or mask[i - cnts[j] - 1] == '#':
				continue
			for k in range(cnts[j]):
				if mask[i - 1 - k] == '.':
					break
			else:
				# it's possible to place cnt[j] at this position
				k = i - cnts[j] - 1
				if j == 0:
					if mask[:k].count('#') == 0:
						d[i][j] = 1
				else:
					while k >= 0 and mask[k] != '#':
						d[i][j] += d[k][j - 1]
						k -= 1

	# print(mask)
	# for line in d:
	# 	print(line)

	result = 0
	for i in range(len(mask)):
		if mask[i:].count('#') == 0:
			result += d[i][-1]

	return result


lines = [line.strip() for line in f.readlines()]
result = 0
for line in lines:
	mask, cnts = line.strip().split()
	cnts = [int(a) for a in cnts.split(',')]
	# mask = '.' + mask + '.'  # task a
	mask = '.' + '?'.join([mask] * 5) + '.'  # task b
	cnts *= 5  # task b
	num = solve(mask, cnts)
	print(num)
	result += num
print(result)