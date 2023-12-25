import copy
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


def remove_brick(brick, a):
	for i in range(brick[0][0], brick[0][1] + 1):
		for j in range(brick[1][0], brick[1][1] + 1):
			for k in range(brick[2][0], brick[2][1] + 1):
				a[i][j][k] = -1


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
	moved = False
	while 1:
		brick = bricks[index]
		if not can_down(brick, a):
			break
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
		moved = True
		# print('moved down brick #', index, brick)
	return moved


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
num_fall = [0] * len(bricks)
result_A = 0
result_B = 0
for index, brick in enumerate(bricks):
	# test if we can remove the brick 
	a_c = copy.deepcopy(a)
	bricks_c = copy.deepcopy(bricks)
	remove_brick(brick, a_c)
	cur_fall = 0
	for i, another_brick in enumerate(bricks_c):
		if i == index: 
			continue
		is_fallen = fall_down(i, a_c, bricks_c)
		if is_fallen:
			cur_fall += 1
	if cur_fall == 0:
		result_A += 1
	result_B += cur_fall
	print(index, cur_fall)

print(result_A)
print(result_B)