f = open("test.in")
f = open("input.txt")

a = [line.strip() for line in f.readlines()]
rows = len(a)
cols = len(a[0])
a = [[int(a[i][j]) for j in range(cols)] for i in range(rows)]

INF = 99

adj = ((0, 1), (0, -1), (1, 0), (-1, 0))

def bfs(r, c):
	# part 1
	d = [[INF] * cols for _ in range(rows)]
	d[r][c] = 0
	# part 2
	d = [[0] * cols for _ in range(rows)]
	d[r][c] = 1

	for step in range(0, 10):
		for i in range(max(r - 10, 0), min(r + 10, rows)):
			for j in range(max(c - 10, 0), min(c + 10, cols)):
				if a[i][j] == step:
					for edge in adj:
						ni = i + edge[0]
						nj = j + edge[1]
						if 0 <= ni < rows and 0 <= nj < cols:
							if a[ni][nj] == a[i][j] + 1:
								# part 1
								# d[ni][nj] = min(d[ni][nj], d[i][j] + 1)
								# part 2
								d[ni][nj] += d[i][j]

	# part 1
	# return sum([d[i].count(9) for i in range(rows)])

	# part 2
	result = 0
	for i in range(max(r - 10, 0), min(r + 10, rows)):
		for j in range(max(c - 10, 0), min(c + 10, cols)):
			if a[i][j] == 9:
				result += d[i][j]
	return result


result = 0
for i in range(rows):
	for j in range(cols):
		if a[i][j] == 0:
			result += bfs(i, j)
print(result)