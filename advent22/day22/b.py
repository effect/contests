# f = open("test.in")
f = open("input.txt")

lines = [line.strip("\n") for line in f.readlines()]

command = lines[-1]
field = lines[:-2]

N = 50
NR = len(field)
NC = max([len(field[ri]) for ri in range(len(field))])

numbers = command.replace('L', ' ').replace('R', ' ').split()
numbers = [int(x) for x in numbers]
# print(max(numbers))
# print(sum(numbers))
print("\n".join(field))


# rn, cn, d -> rn_next, cn_next, d_next
def connect_edges(field, N):
	next_cell = {}
	# connect back and bottom faces
	rn = 0
	cn = N
	d = 3
	rn_next = 3 * N
	cn_next = 0
	d_next = 0
	for i in range(N):
		next_cell[ (rn, cn + i, d) ] = (rn_next + i, cn_next, d_next)
		next_cell[ (rn_next + i, cn_next, (d_next + 2) % 4)  ] = (rn, cn + i, (d + 2) % 4  )

	# connect back and left
	rn = 0
	cn = N
	d = 2
	rn_next = 3 * N - 1
	cn_next = 0
	d_next = 0
	for i in range(N):
		next_cell[ (rn + i, cn, d) ] = (rn_next - i, cn_next, d_next)
		next_cell[ (rn_next - i, cn_next, (d_next + 2) % 4) ] = (rn + i, cn, (d + 2) % 4) 

	# connect right and bottom
	rn = 0
	cn = 2 * N
	d = 3
	rn_next = 4 * N - 1
	cn_next = 0
	d_next = 3
	for i in range(N):
		next_cell[ (rn, cn + i, d) ] = (rn_next, cn_next + i, d_next)
		next_cell[ (rn_next, cn_next + i, (d_next + 2) % 4) ] = (rn, cn + i, (d + 2) % 4)

	# connect right and front
	rn = 0
	cn = 3 * N - 1
	d = 0
	rn_next = 3 * N - 1
	cn_next = 2 * N - 1
	d_next = 2
	for i in range(N):
		next_cell[ (rn + i, cn, d) ] = (rn_next - i, cn_next, d_next)
		next_cell[ (rn_next - i, cn_next, (d_next + 2) % 4) ] =  (rn + i, cn, (d + 2) % 4)

	# connect right and top
	rn = N - 1
	cn = 2 * N
	d = 1
	rn_next = N
	cn_next = 2 * N - 1
	d_next = 2
	for i in range(N):
		next_cell[ (rn, cn + i, d) ] = (rn_next + i, cn_next, d_next)
		next_cell[ (rn_next + i, cn_next, (d_next + 2) % 4) ]	= (rn, cn + i, (d + 2) % 4) 

	# connect top and left
	rn = N
	cn = N
	d = 2
	rn_next = 2 * N
	cn_next = 0
	d_next = 1
	for i in range(N):
		next_cell[ (rn + i, cn, d) ] = (rn_next, cn_next + i, d_next)
		next_cell[ (rn_next, cn_next + i, (d_next + 2) % 4) ] = (rn + i, cn, (d + 2) % 4)

	# connect front and bottom
	rn = 3 * N - 1
	cn = N
	d = 1
	rn_next = 3 * N
	cn_next = N - 1
	d_next = 2
	for i in range(N):
		next_cell[ (rn, cn + i, d) ] = (rn_next + i, cn_next, d_next)
		next_cell[ (rn_next + i, cn_next, (d_next + 2) % 4) ] = (rn, cn + i, (d + 2) % 4)

	return next_cell

next_cell = connect_edges(field, N)



rn = 0
cn = field[rn].index('.')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
d = 0

number_index = 0


def make_step():
	global field, rn, cn, dr, dc, d, NR, NC, next_cell
	
	if (rn, cn, d) in next_cell:
		(rn_next, cn_next, d_next) = next_cell[(rn, cn, d)]
	else:
		rn_next = rn + dr[d]
		cn_next = cn + dc[d]
		d_next = d

	if field[rn_next][cn_next] == '.':
		rn = rn_next
		cn = cn_next
		d = d_next
		return True
	elif field[rn_next][cn_next] == '#':
		return False
	else:
		raise "Out of bounds"

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


rn += 1
cn += 1
print(rn, cn)
result = 1000 * rn + 4 * cn + d
print(result)