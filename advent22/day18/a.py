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

cubes = set([parse_cube(line.strip()) for line in f.readlines()])
num_adjacent = 0

for cube in cubes:
	for coord in range(len(cube)):
		for delta in (-1, 1):
			adj_cube = get_adjacent_cube(cube, coord, delta)
			if adj_cube in cubes:
				num_adjacent += 1

print(6 * len(cubes) - num_adjacent)