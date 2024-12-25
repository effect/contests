f = open("test.in")
f = open("input.txt")
INF = 999999999

lines = [line.strip() for line in f.readlines()]
n = len(lines)
dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]

sr = n - 2
sc = 1
sd = 0
fr = 1
fc = n - 2
print(lines[sr][sc], lines[fr][fc])

d = dict()
d[(sr, sc, 0)] = 0

prev = dict()

def print_result():
	result = INF
	for dirind in range(4):
		result = min(result, d.get((fr, fc, dirind), INF))
	print(result)
	return result


can = set()
sit = set()
def output(i, j, dirind):
	# print(i, j, dirind)
	can.add((i, j, dirind))
	sit.add((i, j))
	if i == sr and j == sc:
		return
	for ni, nj, ndirind in prev[(i, j, dirind)]:
		output(ni, nj, ndirind)


# for it in range(n * n * 4):
for it in range(500):
	print(it, end=' ')
	print_result()

	for i in range(n):
		for j in range(n):
			for dirind in range(4):
				dist = d.get((i, j, dirind), INF)
				if dist < INF:
					ni = i + dir[dirind][0]
					nj = j + dir[dirind][1]
					if lines[ni][nj] != '#':
						if d.get((ni, nj, dirind), INF) > dist + 1:
							d[(ni, nj, dirind)] = dist + 1
							prev[(ni, nj, dirind)] = set()
							prev[(ni, nj, dirind)].add((i, j, dirind))
						elif d.get((ni, nj, dirind), INF) == dist + 1:
							prev[(ni, nj, dirind)].add((i, j, dirind))

					ndirind = (dirind + 1) % 4
					if d.get((i, j, ndirind), INF) > dist + 1000:
						d[(i, j, ndirind)] = dist + 1000
						prev[(i, j, ndirind)] = set()
						prev[(i, j, ndirind)].add((i, j, dirind))
					elif d.get((i, j, ndirind), INF) == dist + 1000:
						prev[(i, j, ndirind)].add((i, j, dirind))

					ndirind = (dirind - 1) % 4
					if d.get((i, j, ndirind), INF) > dist + 1000:
						d[(i, j, ndirind)] = dist + 1000
						prev[(i, j, ndirind)] = set()
						prev[(i, j, ndirind)].add((i, j, dirind))
					elif d.get((i, j, ndirind), INF) == dist + 1000:
						prev[(i, j, ndirind)].add((i, j, dirind))

result = print_result()
for dirind in range(4):
	if d[(fr, fc, dirind)] == result:
		output(fr, fc, dirind)
print(len(sit))