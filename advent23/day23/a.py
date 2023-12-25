import sys
sys.setrecursionlimit(10000)

f = open("test.in")
f = open("input.txt")

a = [line.strip() for line in f.readlines()]
n = len(a)
print(n)
print(a[0][1])
print(a[n - 2][n - 2])

D = ((0, 1), (0, -1), (-1, 0), (1, 0))

def dfs(r, c, pr, pc, len):
	if r == n - 2 and c == n - 2:
		yield len
	for dr, dc in D:
		nr = r + dr
		nc = c + dc
		if nr < 0 or nr >= n or nc < 0 or nc >= n:  # out of bounds
			continue
		if nr == pr and nc == pc:  # previous cell
			continue
		if a[nr][nc] == '#':
			continue
		if a[r][c] == '>' and not (dr, dc) == (0, 1):
			continue
		if a[r][c] == 'v' and not (dr, dc) == (1, 0):
			continue
		yield from dfs(nr, nc, r, c, len + 1)


result = list(dfs(0, 1, 0, 0, 1))
print(result)
print(max(result))