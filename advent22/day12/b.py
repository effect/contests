# f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]
N = len(lines)
M = len(lines[0])
INF = 1000000
EDGES = ( (0, 1), (0, -1), (1, 0), (-1, 0) )

d = [[INF] * M for _ in range(N)]
q = []
lines = [line.replace('S', 'a') for line in lines]

for i, a in enumerate(lines):
	for j, c in enumerate(a):
		if c == 'a':
			q.append((i, j))
			d[i][j] = 0
	if 'E' in a:
		j = a.index('E')
		end_i = i
		end_j = j
		lines[i] = lines[i].replace('E', 'z')

while d[end_i][end_j] == INF:
	i, j = q.pop(0)
	for edge in EDGES:
		next_i = i + edge[0]
		next_j = j + edge[1]
		if 0 <= next_i < N and 0 <= next_j < M:
			if ord(lines[i][j]) + 1 >= ord(lines[next_i][next_j]):
				if d[next_i][next_j] > d[i][j] + 1:
					d[next_i][next_j] = d[i][j] + 1
					q.append((next_i, next_j))

print(d[end_i][end_j])