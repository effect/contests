MIN = 7
MAX = 27

MIN = 200000000000000
MAX = 400000000000000


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

def get_intersection_time(a, b):
	a1 = a[1][0]
	b1 = -b[1][0]
	c1 = b[0][0] - a[0][0]
	a2 = a[1][1]
	b2 = -b[1][1]
	c2 = b[0][1] - a[0][1]

	d = det(a1, b1, a2, b2)
	dt1 = det(c1, b1, c2, b2)
	dt2 = det(a1, c1, a2, c2)
	if d == 0:
		return (-1, -1)
	return (dt1 / d, dt2 / d)

def get_coordinate(a, index, time):
	return a[0][index] + time * a[1][index]


stones = []
for line in lines:
	stones.append(parse_stone(line))

result = 0
for i in range(len(stones)):
	for j in range(i + 1, len(stones)):
		ti, tj = get_intersection_time(stones[i], stones[j])
		if ti >= 0 and tj >= 0:
			coordinates = get_coordinate(stones[i], 0, ti), get_coordinate(stones[i], 1, ti), get_coordinate(stones[j], 0, tj), get_coordinate(stones[j], 1, tj)
			inside = True
			for c in coordinates:
				if not (MIN <= c <= MAX):
					inside = False
					break
			if inside:
				result += 1
				# print(i, j, coordinates)
print(result)
