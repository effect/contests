from queue import Queue

f = open("test.in")
f = open("input.txt")

INF = 999999
THR = 100
DEPTH = 2  # part 1
DEPTH = 20 # part 2

adj = ((0, 1), (1, 0), (0, -1), (-1, 0))

lines = [line.strip() for line in f.readlines()]
n = len(lines)
a = [[INF] * n for _ in range(n)]
for i in range(n):
	for j in range(n):
		if lines[i][j] == '#':
			a[i][j] = -1
		if lines[i][j] == 'S':
			si = i
			sj = j
		if lines[i][j] == 'E':
			fi = i
			fj = j

i, j = si, sj
a[i][j] = 0
while not ((i == fi) and (j == fj)):
	for edge in adj:
		ni, nj = i + edge[0], j + edge[1]
		if a[ni][nj] > a[i][j]:
			a[ni][nj] = a[i][j] + 1
			i, j = ni, nj

# print(a[fi][fj])
# print(sum([lines[i].count('.') for i in range(n)]))
# all empty cells belong to path from S to E

result = 0
i, j = si, sj
while not ((i == fi) and (j == fj)):
	q = Queue()
	visited = set()

	for edge in adj:
		ni, nj = i + edge[0], j + edge[1]
		q.put((ni, nj, 1))
		visited.add((ni, nj))	

	while not q.empty():
		ni, nj, dist = q.get()
		for edge in adj:
			nni, nnj = ni + edge[0], nj + edge[1]
			if 0 <= nni < n and 0 <= nnj < n:
				if (nni, nnj) in visited:
					continue
				if dist + 1 < DEPTH:
					q.put((nni, nnj, dist + 1))
					visited.add((nni, nnj))
				if a[nni][nnj] - a[i][j] - dist - 1 >= THR:
					result += 1
					visited.add((nni, nnj))
					
	for edge in adj:
		ni, nj = i + edge[0], j + edge[1]
		if a[ni][nj] == a[i][j] + 1:
			i, j = ni, nj
			break
print(result)