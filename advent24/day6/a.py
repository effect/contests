f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]
rows = len(lines)
cols = len(lines[0])

a = [[0] * cols for _ in range(rows)]

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
a[ci][cj] = 1

def step(i, j, di, dj):
	ti = i + di
	tj = j + dj
	if not ((0 <= ti < rows) and (0 <= tj < cols)):
		return ti, tj, di, dj
	if a[ti][tj] == -1:
		ti = i
		tj = j
		di, dj = dj, -di
	a[ti][tj] = 1
	return ti, tj, di, dj

def sim(i, j, di, dj):
	while True:
		i, j, di, dj = step(i, j, di, dj)
		if not ((0 <= i < rows) and (0 <= j < cols)):
			return

sim(ci, cj, di, dj)
result = sum([a[i].count(1) for i in range(rows)])
print(result)

