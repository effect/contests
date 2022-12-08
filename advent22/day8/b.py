# f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]
lines = [[int(line[i]) for i in range(len(line))] for line in lines]

result = 0

for j in range(1, len(lines[0]) -  1):
	for i in range(1, len(lines) - 1):
		left, right, up, down = 0, 0, 0, 0
		cur = lines[i][j]

		for jj in range(j - 1, -1, -1):
			left += 1
			if lines[i][jj] >= cur:
				break

		for jj in range(j + 1, len(lines[0])):
			right += 1
			if lines[i][jj] >= cur:
				break

		for ii in range(i - 1, -1, -1):
			up += 1
			if lines[ii][j] >= cur:
				break

		for ii in range(i + 1, len(lines)):
			down += 1
			if lines[ii][j] >= cur:
				break

		# print(left, right, up, down)
		cur = left * right * up * down
		result = max(result, cur)

print(result)

