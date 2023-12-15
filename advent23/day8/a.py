f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

lr = lines[0]
left = {}
right = {}

for line in lines[2:]:
	fr, to = line.split('=')
	fr = fr.strip()
	to = to.strip()[1:-1]
	to_l, to_r = to.split(',')
	left[fr] = to_l.strip()
	right[fr] = to_r.strip()

steps = 0
index = 0
vertex = 'AAA'
while vertex != 'ZZZ':
	cur_direction = lr[index]
	index = (index + 1) % len(lr)
	if cur_direction == 'L':
		vertex = left[vertex]
	else:
		vertex = right[vertex]
	steps += 1
print(steps)
