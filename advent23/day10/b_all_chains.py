from queue import Queue

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


def get_connected_empty(row, col):
	result = []
	dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
	for (dr, dc) in dir:
		r = row + dr
		c = col + dc
		if in_bounds(r, c) and lines[r][c] in ['.', ' ']:
			result.append((r, c))
	return result


# find S
srow = scol = -1
for i in range(nrows):
	for j in range(ncols):
		if lines[i][j] == 'S':
			srow = i
			scol = j
			break


# enlarge field
ext_lines = [' ' + ' '.join(c for c in line) + ' ' for line in lines]
ext_ncols = len(ext_lines[0])
ext_lines = [ext_lines[i // 2] if i % 2 == 1 else ' ' * ext_ncols for i in range(len(ext_lines) * 2 + 1)]
ext_nrows = len(ext_lines)

for line in lines:
	print(line)

# add extra borders
d = [[-1] * ncols for _ in range(nrows)]
for ii in range(nrows):
	for jj in range(ncols):
		if lines[ii][jj] != '.' and d[ii][jj] == -1:
			q = Queue()
			d[ii][jj] = 0
			q.put((ii, jj))
			while not q.empty():
				i, j = q.get()
				adj = get_connected(i, j)
				for (ni, nj) in adj:
					# add border
					ext_i = 2 * i + 1
					ext_j = 2 * j + 1
					ext_ni = 2 * ni + 1
					ext_nj = 2 * nj + 1
					mid_i = (ext_i + ext_ni) // 2
					mid_j = (ext_j + ext_nj) // 2
					ext_lines[mid_i] = ext_lines[mid_i][:mid_j] + "x" + ext_lines[mid_i][mid_j + 1:]
					if d[ni][nj] == -1:
						q.put((ni, nj))
						d[ni][nj] = d[i][j] + 1


lines = ext_lines
ncols = ext_ncols
nrows = ext_nrows
for line in lines:
	print(line)



d = [[-1] * ncols for _ in range(nrows)]
q = Queue()

for i in range(ncols):
	d[0][i] = 0
	q.put((0, i))
	d[nrows - 1][i] = 0
	q.put((nrows - 1, i))
for i in range(nrows):
	d[i][0] = 0
	q.put((i, 0))
	d[i][ncols - 1] = 0
	q.put((i, ncols - 1))



while not q.empty():
	i, j = q.get()
	adj = get_connected_empty(i, j)
	for (ni, nj) in adj:
		if d[ni][nj] == -1:
			d[ni][nj] = d[i][j] + 1
			q.put((ni, nj))

for line in d:
	print(line)

result = 0
for i in range(nrows):
	for j in range(ncols):
		if lines[i][j] == '.' and d[i][j] == -1:
			result += 1
print(result)
