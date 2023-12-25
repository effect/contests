# it takes ~15 min to get the answer for the task B
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
max_path = 0

def dfs(r, c, pr, pc, path):
	if r == n - 2 and c == n - 2:
		global max_path
		if max_path < len(path):
			max_path = len(path)
			print(max_path)  # to track progress
		yield len(path)
	next_options = []
	for dr, dc in D:
		nr = r + dr
		nc = c + dc
		if nr < 0 or nr >= n or nc < 0 or nc >= n:  # out of bounds
			continue
		if nr == pr and nc == pc:  # previous cell
			continue
		if a[nr][nc] == '#':
			continue
		if (nr, nc) in path:
			continue
		next_options.append((nr, nc))

	if len(next_options) == 1:
		nr, nc = next_options[0]
		path.add((nr, nc))
		yield from dfs(nr, nc, r, c, path)
	elif len(next_options) > 1:
		for nr, nc in next_options:
			path_c = path.copy()
			path_c.add((nr, nc))
			yield from dfs(nr, nc, r, c, path_c)


result = [a for a in dfs(0, 1, 0, 0, {(0, 1)})]
print(result)
print(max(result))
