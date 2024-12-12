f = open("test.in")
f = open("input.txt")

a = [line.strip() for line in f.readlines()]

rows = len(a)
cols = len(a[0])

comp = [[-1] * cols for _ in range(rows)]
components = 0

next = ((0, 1), (1, 0), (0, -1), (-1, 0))

def dfs(r, c, color):
	comp[r][c] = color
	for edge in next:
		nr = r + edge[0]
		nc = c + edge[1]
		if 0 <= nr < rows and 0 <= nc < cols and a[r][c] == a[nr][nc] and comp[nr][nc] == -1:
			dfs(nr, nc, color)


for i in range(rows):
	for j in range(cols):
		if comp[i][j] == -1:
			dfs(i, j, components)
			components += 1

# print(comp)

area = [0] * components
perimeter = [0] * components  # part 1
corners = [0] * components  # part 2: number of sides == number of corners

for r in range(rows):
	for c in range(cols):
		cc = comp[r][c]
		area[cc] += 1
		for i in range(len(next)):
			edge = next[i]
			nr = r + edge[0]
			nc = c + edge[1]
			is_next_same = (0 <= nr < rows and 0 <= nc < cols and comp[nr][nc] == comp[r][c])
			# part 1
			if not is_next_same:
				perimeter[cc] += 1

			# part 2
			diag_r = nr
			diag_c = nc
			edge = next[(i + 1) % len(next)]
			nr = r + edge[0]
			nc = c + edge[1]
			diag_r += edge[0]
			diag_c += edge[1]
			is_next_same2 = (0 <= nr < rows and 0 <= nc < cols and comp[nr][nc] == comp[r][c])
			# convex corner
			if (not is_next_same) and (not is_next_same2):
				corners[cc] += 1
			# concave corner
			if (is_next_same) and (is_next_same2):
				is_diag_same = (0 <= diag_r < rows and 0 <= diag_c < cols and comp[diag_r][diag_c] == comp[r][c])
				if not is_diag_same:
					corners[cc] += 1

# part 1
result = 0
for c in range(components):
	result += area[c] * perimeter[c]
print(result)

# part 2
result = 0
for c in range(components):
	# print(area[c], corners[c])
	result += area[c] * corners[c]
print(result)