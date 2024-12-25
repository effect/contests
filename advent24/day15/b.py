import copy

f = open("test.in")
f = open("input.txt")

def output(a, ci, cj):
	n = len(a)
	for i in range(n):
		for j in range(2 * n):
			if i == ci and j == cj:
				print('@', end='')
			else:
				if a[i][j] == 1:
					print('[', end='')
				if a[i][j] == 2:
					print(']', end='')					
				if a[i][j] == 0:
					print('.', end='')
				if a[i][j] == -1:
					print('#', end='')
		print()
	print()


def adj_column(a, row, col):
	if a[row][col] == 1:
		return col + 1
	if a[row][col] == 2:
		return col - 1
	if a[row][col] == 0:
		return -1 
	print("WTF: ", row, col, a[row][col])
	return "WTF"


def extend(a, row, cols):
	result = set(cols)
	for c in cols:
		adj = adj_column(a, row, c)
		if adj >= 0:
			result.add(adj)
	return result


def can_vertical_move(a, row, col, dr):
	r = row
	cols = {col}
	while len(cols):
		can_move = True
		next_level = set()
		nr = r + dr		
		for c in cols:
			if a[nr][c] == -1:
				can_move = False
				break
			if a[nr][c] >= 1:
				next_level.add(c)
		if not can_move:
			return False
		cols = extend(a, nr, next_level)
		r += dr
	return True


def make_vertical_move(a, row, col, dr):
	r = row
	cols = {col, adj_column(a, row, col)}
	to_free = list(cols)
	save = a[r][:]
	while len(cols):
		next_level_full = set()
		next_level_move = set()

		nr = r + dr	
		for c in cols:
			if a[nr][c] >= 1:
				next_level_move.add(c)
			next_level_full.add(c)
		next_level_full = extend(a, nr, next_level_full)
		next_level_move = extend(a, nr, next_level_move)

		save_new = a[nr][:]
		for c in next_level_full:
			a[nr][c] = save[c] if c in cols else 0
		save = save_new[:]

		r += dr
		cols = next_level_move

	for c in to_free:
		a[row][c] = 0



def make_horizontal_move(a, row, col, dc):
	nc = col
	save = a[row][nc]
	while save >= 1:
		nc += dc
		save, a[row][nc] = a[row][nc], save


lines = [line.strip() for line in f.readlines()]
n = len(lines[0])
a = [[0] * 2 * n for _ in range(n)]
ci = cj = 0
for i in range(n):
	for j in range(n):
		if lines[i][j] == '#':
			a[i][2 * j] = -1
			a[i][2 * j + 1] = -1
		if lines[i][j] == 'O':
			a[i][2 * j] = 1
			a[i][2 * j + 1] = 2
		if lines[i][j] == '@':
			ci = i
			cj = 2 * j

steps = "".join(lines[n + 1:])

d = {'>': (0, 1), '<': (0, -1), 'v': (1, 0), '^': (-1, 0)}
for step in steps:
	# output(a, ci, cj)
	# print(step)

	di, dj = d[step]
	ni = ci + di
	nj = cj + dj 
	# print(ci, cj, ni, nj)
	if a[ni][nj] == -1:
		# stay in ci, cj
		continue
	if a[ni][nj] == 0:
		# move to ni, nj
		ci = ni
		cj = nj
		continue
	# a[ni][nj] == 1 or 2 , i.e. box
	if di == 0:
		# horizontal move - same logic as part 1	
		while a[ni][nj] >= 1:
			ni += di
			nj += dj
		if a[ni][nj] == 0:
			# can move boxes
			# move the row
			make_horizontal_move(a, ci, cj + dj, dj)
			a[ci][cj + dj] = 0
			# move to the next cell
			ci += di
			cj += dj 
		elif a[ni][nj] == -1:
			# can't move, stay in ci, cj
			continue
	else:
		if can_vertical_move(a, ci, cj, di):
			make_vertical_move(a, ci + di, cj, di)
			ci += di
			

result = 0
for i in range(n):
	for j in range(2 * n):
		if a[i][j] == 1:
			result += 100 * i + j
print(result)