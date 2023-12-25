f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

def parse_point(line):
	coord = line.split(', ')
	coord = tuple(int(x) for x in coord)
	return coord

def parse_stone(line):
	start, velocity = line.split(' @ ')
	return (parse_point(start), parse_point(velocity))

def det(a1, b1, a2, b2):
	return a1 * b2 - a2 * b1

def get_coordinate(a, index, time):
	return a[0][index] + time * a[1][index]

def sub_vector(a, b):
	return (a[0] - b[0], a[1] - b[1], a[2] - b[2])

def add_vector(a, b):
	return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


# get plane by three points: A, B and O(0, 0, 0)
def get_zero_plane(A, B):
	x2, y2, z2 = A
	x3, y3, z3 = B
	a = det(y2, z2, y3, z3)
	b = -det(x2, z2, x3, z3)
	c = det(x2, y2, x3, y3)
	return (a, b, c)

def intersect_plane_line(plane, line):
	s, v = line
	a, b, c = plane
	time = -(a * s[0] + b * s[1] + c * s[2]) / (a * v[0] + b * v[1] + c * v[2])
	point = tuple(get_coordinate(line, i, time) for i in range(3))
	return point, time

def get_velocity(x1, t1, x2, t2):
	return (x2 - x1) / (t2 - t1)

def get_start(x1, t1, vx):
	return x1 - t1 * vx

def check_in_plane(point, plane):
	return point[0] * plane[0] + point[1] * plane[1] + point[2] * plane[2]

stones = []
for line in lines:
	stones.append(parse_stone(line))

# move to coordinate system associated with first stone (stone[0])
print(stones)
first_stone = stones[0]
stones = [(sub_vector(stone[0], first_stone[0]), sub_vector(stone[1], first_stone[1])) for stone in stones]
print(stones)

# find plane that goes through O and line(stone[1])
# rock's line lies in that plane
A = stones[1][0]  # point at time = 0
B = add_vector(stones[1][0], stones[1][1])  # point at time = 1
print(A, B)
zero_plane = get_zero_plane(A, B)
print(zero_plane)

# intersect some other two lines with the plane
A, ta = intersect_plane_line(zero_plane, stones[2])
B, tb = intersect_plane_line(zero_plane, stones[4])
print(A, ta)
print(B, tb)
print(check_in_plane(A, zero_plane))
print(check_in_plane(B, zero_plane))

rock_velocity = tuple(get_velocity(A[i], ta, B[i], tb) for i in range(3))
rock_start = tuple(get_start(A[i], ta, rock_velocity[i]) for i in range(3))

# move back to original coordinates
rock_start = add_vector(rock_start, first_stone[0])
rock_velocity = add_vector(rock_velocity, first_stone[1])

print(rock_velocity)
print(rock_start)

result = sum(rock_start)
print(result)