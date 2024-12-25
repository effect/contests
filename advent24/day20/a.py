f = open("test.in")
f = open("input.txt")

INF = 999999
THR = 100

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
	# print(a[i][j], i, j)
	for edge in adj:
		ni, nj = i + edge[0], j + edge[1]
		if a[ni][nj] == -1:
			# try to break this wall
			for e in adj:
				nni, nnj = ni + e[0], nj + e[1]
				if 0 <= nni < n and 0 <= nnj < n:
					if a[nni][nnj] < INF and a[nni][nnj] - a[i][j] - 2 >= THR:
						result += 1 
						# print(a[nni][nnj] - a[i][j] - 2, i, j, nni, nnj)
			# nni, nnj = ni + edge[0], nj + edge[1]
			# if 0 <= nni < n and 0 <= nnj < n:
			# 	if a[nni][nnj] < INF and a[nni][nnj] - a[i][j] - 2 >= THR:
			# 		result += 1 

	for edge in adj:
		ni, nj = i + edge[0], j + edge[1]
		if a[ni][nj] == a[i][j] + 1:
			i, j = ni, nj
			break
print(result)