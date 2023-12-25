INF = 999
f = open("test.in")
f = open("input.txt")


def get_brick(line):
	a, b = line.split('~')
	a = a.split(',')
	a = [int(x) for x in a]
	b = b.split(',')
	b = [int(x) for x in b]
	result = list(zip(a, b))
	result[-1] = (min(result[-1]), max(result[-1]))
	return result


def add_brick(brick, index, a):
	for i in range(brick[0][0], brick[0][1] + 1):
		for j in range(brick[1][0], brick[1][1] + 1):
			for k in range(brick[2][0], brick[2][1] + 1):
				a[i][j][k] = index


def can_down(brick, a):
	z = brick[-1][0]
	if z <= 1:
		return False
	for i in range(brick[0][0], brick[0][1] + 1):
		for j in range(brick[1][0], brick[1][1] + 1):
			if a[i][j][z - 1] >= 0:
				return False
	return True


def fall_down(index, a, bricks):
	while 1:
		brick = bricks[index]
		if not can_down(brick, a):
			return
		if brick[-1][0] == brick[-1][1]:
			# horizontal brick
			z = brick[-1][0]
			for i in range(brick[0][0], brick[0][1] + 1):
				for j in range(brick[1][0], brick[1][1] + 1):
					a[i][j][z] = -1
					a[i][j][z - 1] = index
		else:
			# vertical brick
			x = brick[0][0]
			y = brick[1][0]
			a[x][y][brick[-1][1]] = -1
			a[x][y][brick[-1][0] - 1] = index

		bricks[index][-1] = (brick[-1][0] - 1, brick[-1][1] - 1)
		# print('moved down brick #', index, brick)

def num_below_adjacent(brick, a):
	z = brick[-1][0]
	if z <= 1:
		return INF
	below = set()
	for i in range(brick[0][0], brick[0][1] + 1):
		for j in range(brick[1][0], brick[1][1] + 1):
			if a[i][j][z - 1] >= 0:
				below.add(a[i][j][z - 1])
	return len(below)


lines = [line.strip() for line in f.readlines()]
bricks = []

N = 10
Z = 0
for line in lines:
	brick = get_brick(line)
	Z = max(Z, max(brick[-1]))
	bricks.append(brick)

Z += 2
a = [[[-1] * Z for i in range(N)] for j in range(N)]
bricks = sorted(bricks, key=lambda brick: brick[-1][0])

print(bricks)
for index, brick in enumerate(bricks):
	add_brick(brick, index, a)
for index, brick in enumerate(bricks):
	fall_down(index, a, bricks)

print(bricks)

num_below = [num_below_adjacent(brick, a) for brick in bricks]
print(num_below)
result = 0
for index, brick in enumerate(bricks):
	# test if we can remove the brick 
	z = brick[-1][1]
	can_remove = True
	for i in range(brick[0][0], brick[0][1] + 1):
		for j in range(brick[1][0], brick[1][1] + 1):
			adj_brick = a[i][j][z + 1]
			if adj_brick >= 0:
				if num_below[adj_brick] <= 1:
					can_remove = False
	if can_remove:
		print('can remove brick #', index)
		result += 1
print(result)