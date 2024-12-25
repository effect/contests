import re

f = open("test.in")
f = open("input.txt")

MAX = 101
INF = 999

lines = [line.strip() for line in f.readlines()]

def get_numbers(line, sign):
	# match numbers after + or =
	matches = re.findall(rf'\{sign}(\d+)', line)
	ax, ay = map(int, matches)
	return ax, ay  # part 1


def tokens(ax, ay, bx, by, x, y):
	num = y * bx - x * by
	den = ay * bx - ax * by
	if num % den == 0:
		na = num // den
		nb = (x - na * ax) // bx
		return 3 * na + nb
	return 0


result = 0
li = 0
while li < len(lines):
	ax, ay = get_numbers(lines[li], '+')	
	bx, by = get_numbers(lines[li + 1], '+')
	x, y = get_numbers(lines[li + 2], '=')
	
	# part 2
	x += 10000000000000
	y += 10000000000000
	########

	result += tokens(ax, ay, bx, by, x, y)
	li += 4
print(result)