# WRONG, doesn't account for all possible options
f = open("test.in")
# f = open("input.txt")

lines = [line.strip() for line in f.readlines()]
rows = len(lines)
cols = len(lines[0])

a = [[set() for j in range(cols)] for i in range(rows)]

for i in range(rows):
	for j in range(cols):
		if lines[i][j] == "^":
			ci = i
			cj = j
		if lines[i][j] == "#":
			a[i][j] = -1
# init direction ^
di = -1
dj = 0
a[ci][cj].add((di, dj))

def step(i, j, di, dj):
	ti = i + di
	tj = j + dj
	if not ((0 <= ti < rows) and (0 <= tj < cols)):
		return ti, tj, di, dj
	if a[ti][tj] == -1:
		ti = i
		tj = j
		di, dj = dj, -di
	a[ti][tj].add((di, dj))
	return ti, tj, di, dj

def sim(i, j, di, dj):
	options = set()
	while True:
		ni, nj, di, dj = step(i, j, di, dj)
		if not ((0 <= ni < rows) and (0 <= nj < cols)):
			return options
		if (ni, nj) != (i, j):
			# test (i, j)
			change_di, change_dj = dj, -di
			print(i, j, a[i][j])
			if (change_di, change_dj) in a[i][j]:
				print(f"Adding option {(ni, nj)} when stay in position {(i, j)} with direction {(di, dj)}")
				options.add((ni, nj))
		i, j = ni, nj


options = sim(ci, cj, di, dj)
print(len(options))
print(options)

