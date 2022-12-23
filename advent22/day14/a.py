# f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]


def get_x_y(part, x0=0):
	x, y = (int(a) for a in part.split(','))
	x -= x0
	return x, y


min_x = 500
max_x = 500
max_y = 0


for line in lines:
	parts = line.split(" -> ")
	for part in parts:
		x, y = get_x_y(part)
		min_x = min(min_x, x)
		max_x = max(max_x, x)
		max_y = max(max_y, y)

X0 = min_x
max_x = max_x - X0 + 1
max_y += 1
print(X0, max_x, max_y)

a = [[" "] * max_x for i in range(max_y)]

for line in lines:
	parts = line.split(" -> ")
	x_p, y_p = get_x_y(parts[0], X0)
	for part in parts[1:]:
		x_c, y_c = get_x_y(part, X0)
		if x_p != x_c:
			y = y_c
			for x in range( min(x_p, x_c), max(x_p, x_c) + 1 ):
				a[y][x] = "#"
		else:
			x = x_c
			for y in range( min(y_p, y_c), max(y_p, y_c) + 1):
				a[y][x] = "#"
		x_p, y_p = x_c, y_c

# for r in a:
# 	print("".join(r))


moves = ( (0, 1), (-1, 1), (1, 1) )
def fall(x, y):
	for move in moves:
		nx = x + move[0]
		ny = y + move[1]
		if nx < 0 or nx >= max_x or ny >= max_y:
			return False
		if a[ny][nx] == ' ':
			return fall(nx, ny)
	# all moves blocked
	a[y][x] = 'o'
	return True

for iterat in range(1000):
	x = 500 - X0
	y = 0
	result = fall(x, y)
	if not result:
		print(iterat)
		break

# for r in a:
# 	print("".join(r))
