f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

def extend(lines):
	col = len(lines[0]) - 1
	while col >= 0:
		if all([lines[i][col] == '.' for i in range(len(lines))]):
			for i in range(len(lines)):
				lines[i] = lines[i][:col] + "." + lines[i][col:]
		col -= 1

	row = len(lines) - 1
	while row >= 0:
		if all([lines[row][i] == '.' for i in range(len(lines[0]))]):
			lines.insert(row, '.' * len(lines[0]))
		row -= 1

	return lines


lines = extend(lines)

for line in lines:
	print(line)

nodes = []
for i in range(len(lines)):
	for j in range(len(lines[0])):
		if lines[i][j] == '#':
			nodes.append((i, j))

total = 0
for i in range(len(nodes)):
	for j in range(i + 1, len(nodes)):
		r1, c1 = nodes[i]
		r2, c2 = nodes[j]
		total += abs(r1 - r2) + abs(c1 - c2)

print(total)