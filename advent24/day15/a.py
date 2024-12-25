f = open("test.in")
f = open("input.txt")

def output(a):
	n = len(a)
	for i in range(n):
		for j in range(n):
			if a[i][j] == 1:
				print('O', end='')
			if a[i][j] == 0:
				print('.', end='')
			if a[i][j] == -1:
				print('#', end='')
		print()
	print()


lines = [line.strip() for line in f.readlines()]
n = len(lines[0])
a = [[0] * n for _ in range(n)]
ci = cj = 0
for i in range(n):
	for j in range(n):
		if lines[i][j] == '#':
			a[i][j] = -1
		if lines[i][j] == 'O':
			a[i][j] = 1
		if lines[i][j] == '@':
			ci = i
			cj = j

steps = "".join(lines[n + 1:])

d = {'>': (0, 1), '<': (0, -1), 'v': (1, 0), '^': (-1, 0)}
for step in steps:
	# output(a)
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
	while a[ni][nj] == 1:
		ni += di
		nj += dj
	if a[ni][nj] == 0:
		# can move boxes
		# move the row
		a[ni][nj], a[ci + di][cj + dj] = a[ci + di][cj + dj], a[ni][nj]
		# move to the next cell
		ci += di
		cj += dj 
	elif a[ni][nj] == -1:
		# can't move, stay in ci, cj
		continue

result = 0
for i in range(n):
	for j in range(n):
		if a[i][j] == 1:
			result += 100 * i + j
print(result)