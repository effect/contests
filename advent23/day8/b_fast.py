import math 

f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]
lr = lines[0]
left = {}
right = {}
vertices = []
for line in lines[2:]:
	fr, to = line.split('=')
	fr = fr.strip()
	to = to.strip()[1:-1]
	to_l, to_r = to.split(',')
	left[fr] = to_l.strip()
	right[fr] = to_r.strip()
	if fr[-1] == 'A':
		vertices.append(fr)
print(vertices)
print(len(lr))


for vertex in vertices:
	# find a cycle for each starting vertex
	steps = 0
	index = 0
	v = vertex
	# key: (vertex id, index of line)
	# value: number of steps
	visited = {}
	while (v, index) not in visited:
		visited[(v, index)] = steps
		cur_direction = lr[index]
		index = (index + 1) % len(lr)
		if cur_direction == 'L':
			v = left[v]
		else:
			v = right[v]
		steps += 1
	print("Visiting second time: ", v, index)
	print("Number of steps: ", steps)
	print("Prev time visited on step: ", visited[(v, index)])
	print("Length of cycle:", steps - visited[(v, index)])


for vertex in vertices:
	steps = 0
	index = 0
	v = vertex
	# key: (vertex id, index of line)
	# value: number of steps
	visited = {}
	while (v, index) not in visited:
		# find where Z located
		if v[-1] == 'Z':
			print(v, index, steps)
		visited[(v, index)] = steps
		cur_direction = lr[index]
		index = (index + 1) % len(lr)
		if cur_direction == 'L':
			v = left[v]
		else:
			v = right[v]
		steps += 1

print(math.lcm(13201, 22411, 18727, 18113, 16271, 20569))