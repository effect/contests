# f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]
lines = [[int(line[i]) for i in range(len(line))] for line in lines]

result = 2 * (len(lines) + len(lines[0])) - 4

for j in range(1, len(lines[0]) -  1):
	column = [line[j] for line in lines]
	for i in range(1, len(lines) - 1):
		m1 = max(lines[i][:j])
		m2 = max(lines[i][j+1:])
		m3 = max(column[:i])
		m4 = max(column[i+1:])
		cur = lines[i][j]
		if m1 < cur or m2 < cur or m3 < cur or m4 < cur:
			result += 1

print(result)

