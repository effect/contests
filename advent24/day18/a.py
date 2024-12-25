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

for step in range(FALLING):
	i, j = (int(x) for x in lines[step].split(','))
	safe[i][j] = False

for step in range(N * N):
	for i in range(N):
		for j in range(N):
			if safe[i][j] and a[i][j] == step:
				for d in adj:
					ni = i + d[0]
					nj = j + d[1]
					if 0 <= ni < N and 0 <= nj < N and safe[ni][nj]:
						a[ni][nj] = min(a[ni][nj], a[i][j] + 1)

print(a[-1][-1])

