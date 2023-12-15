f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

def get_clean_cols():
	result = []
	for col in range(len(lines[0])):
		if all([lines[i][col] == '.' for i in range(len(lines))]):
			result.append(col)
	return result


def get_clean_rows():
	result = []
	for row in range(len(lines)):
		if all([lines[row][i] == '.' for i in range(len(lines[0]))]):
			result.append(row)
	return result


def num_clean(a, b, clean):
	num = 0
	a, b = min(a ,b), max(a, b)
	for c in clean:
		if a < c < b:
			num += 1
	return num


clean_rows = get_clean_rows()
clean_cols = get_clean_cols()
print(clean_rows)
print(clean_cols)

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
		total += num_clean(r1, r2, clean_rows) * 999999  # multiplier just for b part
		total += num_clean(c1, c2, clean_cols) * 999999  # multiplier just for b part
print(total)