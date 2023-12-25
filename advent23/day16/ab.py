from queue import Queue

f = open("test.in")
f = open("input.txt")

a = [line.strip() for line in f.readlines()]
n = len(a)


def rotate(mirror, dr, dc):
	if mirror == '/':
		return (-dc, -dr)
	if mirror == '\\':
		return (dc, dr)
	print('Unexpected symbol: ', mirror)


def get_next_positions(cell, direction):
	row, col = cell
	dr, dc = direction
	if a[row][col] == '.' or (a[row][col] == '-' and dr == 0) or (a[row][col] == '|' and dc == 0):
		return [((row + dr, col + dc), direction)]
	elif a[row][col] == '-' or a[row][col] == '|':
		dr1, dc1 = dc, dr
		dr2, dc2 = -dc, -dr
		return [((row + dr1, col + dc1), (dr1, dc1)), ((row + dr2, col + dc2), (dr2, dc2))]
	else:
		(dr, dc) = rotate(a[row][col], dr, dc)
		return [((row + dr, col + dc), (dr, dc))]


def in_bounds(cell):
	row, col = cell
	return 0 <= row < n and 0 <= col < n


def num_visited(cell, dir):
	q = Queue()
	q.put((cell, dir))
	visited = set()
	visited.add((cell, dir))
	visited_cells = set()
	visited_cells.add(cell)

	while not q.empty():
		cell, direction = q.get()
		next_positions = get_next_positions(cell, direction)
		for pos in next_positions:
			cell, direction = pos
			if in_bounds(cell) and pos not in visited:
				q.put(pos)
				visited.add(pos)
				visited_cells.add(cell)

	return len(visited_cells)


# task a
cell = (0, 0)
dir = (0, 1)
print(num_visited(cell, dir))

# task b
max_visited = 0
for i in range(n):
	cur = num_visited((i, 0), (0, 1))
	max_visited = max(max_visited, cur)
	cur = num_visited((i, n - 1), (0, -1))
	max_visited = max(max_visited, cur)
	cur = num_visited((0, i), (1, 0))
	max_visited = max(max_visited, cur)	
	cur = num_visited((n - 1, i), (-1, 0))
	max_visited = max(max_visited, cur)	
print(max_visited)