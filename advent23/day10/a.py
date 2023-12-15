f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]
nrows = len(lines)
ncols = len(lines[0])

def in_bounds(row, col):
	return row >= 0 and row < nrows and col >= 0 and col < ncols

def get_connected(row, col):
	result = []
	# test above
	if lines[row][col] in ['S', '|', 'L', 'J']:
		r = row - 1
		c = col
		if in_bounds(r, c) and (lines[r][c] in ['|', '7', 'F']):
			result.append((r, c))

	# test below
	if lines[row][col] in ['S', '|', '7', 'F']:
		r = row + 1
		c = col
		if in_bounds(r, c) and (lines[r][c] in ['|', 'L', 'J']):
			result.append((r, c))

	# test left
	if lines[row][col] in ['S', '-', 'J', '7']:	
		r = row
		c = col - 1
		if in_bounds(r, c) and (lines[r][c] in ['-', 'L', 'F']):
			result.append((r, c))

	# test right 
	if lines[row][col] in ['S', '-', 'L', 'F']:	
		r = row
		c = col + 1
		if in_bounds(r, c) and (lines[r][c] in ['-', 'J', '7']):
			result.append((r, c))

	return result

srow = scol = -1
for i in range(nrows):
	for j in range(ncols):
		if lines[i][j] == 'S':
			srow = i
			scol = j
			break


d = [[-1] * ncols for _ in range(nrows)]
d[srow][scol] = 0

curd = 0
while 1:
	num_new = 0
	for i in range(nrows):
		for j in range(ncols):
			if d[i][j] == curd:
				adj = get_connected(i, j)
				for (ni, nj) in adj:
					if d[ni][nj] == -1:
						d[ni][nj] = curd + 1
						num_new += 1
	if num_new == 0:
		break
	curd += 1


print(curd)
# print(d)
