f = open("test.in")
f = open("input.txt")

def parse_cube(line):
	x, y, z = (int(x) for x in line.split(','))
	return (x, y, z)

def get_adjacent_cube(cube, coord_index, delta):
	if coord_index == 0:
		return (cube[0] + delta, cube[1], cube[2])
	elif coord_index == 1:
		return (cube[0], cube[1] + delta, cube[2])
	if coord_index == 2:
		return (cube[0], cube[1], cube[2] + delta)

def gen_adjacent_cubes(cube):
	cubes = []
	for coord in range(len(cube)):
		for delta in (-1, 1):
			adj_cube = get_adjacent_cube(cube, coord, delta)
			cubes.append(adj_cube)
	return cubes

def gen_ext_cube(coord_index, a, b, c):
	if coord_index == 0:
		return (a, b, c)
	elif coord_index == 1:
		return (b, a, c)
	if coord_index == 2:
		return (b, c, a)


cubes = set([parse_cube(line.strip()) for line in f.readlines()])

# task a
num_adjacent = 0
for cube in cubes:
	for adj_cube in gen_adjacent_cubes(cube):
		if adj_cube in cubes:
			num_adjacent += 1

print(6 * len(cubes) - num_adjacent)


# task b
min_coord = min( [min(cube) for cube in cubes] ) - 1
max_coord = max( [max(cube) for cube in cubes] ) + 1
print(min_coord, max_coord)

def gen_external_cubes():
	ec = set()
	for coord_index in range(3):
		for i in range(min_coord, max_coord + 1):
			for j in range(min_coord, max_coord + 1):
				ec.add( gen_ext_cube(coord_index, min_coord, i, j) )
				ec.add( gen_ext_cube(coord_index, max_coord, i, j) )
	return ec

def is_valid_cube(cube):
	for c in cube:
		if c < min_coord or c > max_coord:
			return False
	return True

q = gen_external_cubes()
visited = set()
num_adjacent_to_external = 0

while len(q) > 0:
	cube = q.pop()
	if cube in visited:
		continue
	visited.add(cube)
	adj_cubes = gen_adjacent_cubes(cube)
	for ac in adj_cubes:
		if not is_valid_cube(ac):
			continue
		if ac in cubes:
			num_adjacent_to_external += 1
		else:
			if ac not in visited:
				q.add(ac)

print(num_adjacent_to_external)