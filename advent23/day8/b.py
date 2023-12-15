f = open("test.in")
f = open("input.txt")

def all_ends_with_z(vertices):
	for v in vertices:
		if v[-1] != 'Z':
			return False
	return True

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

steps = 0
index = 0
while not all_ends_with_z(vertices):
	if steps % 10000 == 0:
		print(steps)
		print(vertices)
	cur_direction = lr[index]
	index = (index + 1) % len(lr)
	for i in range(len(vertices)):
		vertex = vertices[i]
		if cur_direction == 'L':
			vertex = left[vertex]
		else:
			vertex = right[vertex]
		vertices[i] = vertex
	steps += 1
print(steps)
