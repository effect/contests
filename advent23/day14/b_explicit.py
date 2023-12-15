import copy
f = open("test.in")
f = open("input.txt")

a = [list(line.strip()) for line in f.readlines()]
nrow = len(a)
ncol = len(a[0])
print(nrow, ncol)


def in_bounds(row, col):
	return 0 <= row < nrow and 0 <= col < ncol


def bubble(row, col, drow, dcol):
	global a
	if a[row][col] == 'O':
		i = row
		j = col
		ni = i + drow
		nj = j + dcol
		while in_bounds(ni, nj) and a[ni][nj] == '.':
			a[ni][nj] = 'O'
			a[i][j] = '.'
			i = ni
			j = nj 
			ni = i + drow
			nj = j + dcol


def tilt(drow, dcol):
	if dcol == 0:
		for col in range(ncol):
			if drow == -1:				
				for row in range(nrow):
					bubble(row, col, drow, dcol)
			elif drow == 1:
				for row in reversed(range(nrow)):
					bubble(row, col, drow, dcol)
	if drow == 0:
		for row in range(nrow):
			if dcol == -1:
				for col in range(ncol):
					bubble(row, col, drow, dcol)
			elif dcol == 1:
				for col in reversed(range(ncol)):
					bubble(row, col, drow, dcol)


def iteration():
	tilt(-1, 0)
	tilt(0, -1)
	tilt(1, 0)
	tilt(0, 1)


def table_to_str(a):
	return "".join([''.join(line) for line in a])



history = {}
history[table_to_str(a)] = 0
num_iterations = 1000000000
for it in range(1, num_iterations):
	iteration()
	s = table_to_str(a)
	if s in history:
		print("First occurence: ", history[s])
		print("Second occurence: ", it)
		break
	history[s] = it

cycle = it - history[s]
num_iterations -= history[s]
num_iterations %= cycle
for it in range(num_iterations):
	iteration()

# for line in a:
# 	print(''.join(line))

result = 0
for col in range(ncol):
	for row in range(nrow):
		if a[row][col] == 'O':
			result += nrow - row
print(result)
