f = open("test.in")
f = open("input.txt")

lines = [line.strip("\n") for line in f.readlines()]

command = lines[-1]
field = lines[:-2]

NC = max([len(field[ri]) for ri in range(len(field))])
field = [" " + row + " " * (NC - len(row) + 1) for row in field]
NC += 2

field = [" " * NC] + field + [" " * NC]
NR = len(field)

numbers = command.replace('L', ' ').replace('R', ' ').split()
numbers = [int(x) for x in numbers]
print(max(numbers))
print(sum(numbers))
print("\n".join(field))

rn = 1
cn = field[rn].index('.')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
d = 0

number_index = 0


def get_leftmost_nonempty(field, r, c):
	c = 0
	while field[r][c] == ' ':
		c += 1
	return c

def get_rightmost_nonempty(field, r, c):
	global NC
	c = NC - 1
	while field[r][c] == ' ':
		c -= 1
	return c

def get_upper_nonempty(field, r, c):
	r = 0
	while field[r][c] == ' ':
		r += 1
	return r

def get_bottom_nonempty(field, r, c):
	global NR
	r = NR - 1
	while field[r][c] == ' ':
		r -= 1
	return r

def make_step():
	global field, rn, cn, dr, dc, d, NR, NC
	rn_next = rn + dr[d]
	cn_next = cn + dc[d]
	if field[rn_next][cn_next] == '.':
		rn = rn_next
		cn = cn_next
		return True
	elif field[rn_next][cn_next] == ' ':
		# out of bounds => adjust position
		if d == 0:
			cn_next = get_leftmost_nonempty(field, rn_next, cn_next)
		elif d == 1:
			rn_next = get_upper_nonempty(field, rn_next, cn_next)
		elif d == 2:
			cn_next = get_rightmost_nonempty(field, rn_next, cn_next)
		elif d == 3:
			rn_next = get_bottom_nonempty(field, rn_next, cn_next)

	if field[rn_next][cn_next] == '#':
		return False
	
	# else: success
	rn = rn_next
	cn = cn_next
	return True


for i, s in enumerate(command):
	if s == 'R':
		d = (d + 1) % 4
	elif s == 'L':
		d = (d - 1) % 4
	else:
		# number
		if i > 0 and command[i - 1].isdigit():
			# already processed this number
			continue
		else:
			number = numbers[number_index]
			number_index += 1

		for step in range(number):
			moved = make_step()
			if not moved:
				break


print(rn, cn)

result = 1000 * rn + 4 * cn + d
print(result)