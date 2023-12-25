import heapq
f = open("test.in")
f = open("input.txt")

a = [list(line.strip()) for line in f.readlines()]
a = [[int(x) for x in line] for line in a]
n = len(a)

# vertex: (cell, direction): ((row, col), (dr, dc))
d = {}
d[((0, 0), (-1, 0))] = 0
d[((0, 0), (0, -1))] = 0
q = []
heapq.heappush(q, (d[((0, 0), (-1, 0))], ((0, 0), (-1, 0))))
heapq.heappush(q, (d[((0, 0), (0, -1))], ((0, 0), (0, -1))))
DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))
INF = 10 ** 6
# MIN_STEPS = 1  # task A
# MAX_STEPS = 3  # task A
MIN_STEPS = 4    # task B
MAX_STEPS = 10   # task B
while q:
	dist, vertex = heapq.heappop(q)
	(row, col), (dr, dc) = vertex
	for direction in DIRECTIONS:
		if direction == (dr, dc) or direction == (-dr, -dc):
			continue
		add_dist = 0
		nrow = row
		ncol = col
		for step in range(1, MAX_STEPS + 1):
			nrow += direction[0]
			ncol += direction[1]
			if not (0 <= nrow < n and 0 <= ncol < n):
				break
			add_dist += a[nrow][ncol]
			if step < MIN_STEPS:
				continue
			cur_dist = d.get(((nrow, ncol), direction), INF)
			if cur_dist > dist + add_dist:
				d[((nrow, ncol), direction)] = dist + add_dist
				heapq.heappush(q, (d[((nrow, ncol), direction)], ((nrow, ncol), direction)))
result = INF
for direction in DIRECTIONS:
	result = min(result, d.get(((n - 1, n - 1), direction), INF))
print(result)