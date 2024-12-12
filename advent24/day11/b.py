f = open("test.in")
f = open("input.txt")

line = [line.strip() for line in f.readlines()][0]
a = [int(x) for x in line.split()]
NUM = 25  # part 1
NUM = 75  # part 2

def blink_number(x):
	if x == 0:
		return 1
	else:
		strx = str(x)
		if len(strx) % 2 == 0:
			x1 = strx[:len(strx) // 2]
			x2 = strx[len(strx) // 2 : ]
			return int(x1), int(x2)
		else:
			return x * 2024

cache_stones = dict()

def stones(initial, iterations):
	if iterations == 0:
		return 1
	value = cache_stones.get((initial, iterations), -1)
	if value > 0:
		return value
	next_stones = blink_number(initial)
	if type(next_stones) is int:
		value = stones(next_stones, iterations - 1)
	else:
		value = stones(next_stones[0], iterations - 1) + stones(next_stones[1], iterations - 1)
	cache_stones[(initial, iterations)] = value
	return value


result = 0
for x in a:
	result += stones(x, NUM)

print(result)