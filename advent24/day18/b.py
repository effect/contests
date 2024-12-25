import sys
sys.setrecursionlimit(10000)

f = open("test.in")
N = 7
FALLING = 12

f = open("input.txt")
N = 71
FALLING = 1024

lines = [line.strip() for line in f.readlines()]
INF = 9999
safe = [[True] * N for _ in range(N)]
a = [[INF] * N for _ in range(N)]
a[0][0] = 0

adj = ((0, 1), (1, 0), (0, -1), (-1, 0))
visited = [[False] * N for _ in range(N)]

def dfs(i, j):
	if i == N - 1 and j == N - 1:
		return True
	visited[i][j] = True
	result = False
	for d in adj:
		ni = i + d[0]
		nj = j + d[1]
		if 0 <= ni < N and 0 <= nj < N and safe[ni][nj] and not visited[ni][nj]:
			cur = dfs(ni, nj)
			if cur:
				return True
			result |= cur
	return False


for step in range(len(lines)):
	i, j = (int(x) for x in lines[step].split(','))
	safe[i][j] = False
	visited = [[False] * N for _ in range(N)]
	if not dfs(0, 0):
		print(f"{i},{j}")
		break