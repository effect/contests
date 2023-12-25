f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

DIR = {
	'R': (0, 1),
	'L': (0, -1), 
	'U': (-1, 0), 
	'D': (1, 0),  
}

DIR_B = ['R', 'D', 'L', 'U']

vertex = (0, 0)
area = 0
border = 0
for line in lines:
	dir, num, color = line.split()	
	# task A
	# num = int(num)

	# task B
	color = color[2:-1]
	dir = DIR_B[int(color[-1])]
	num = int(color[:-1], 16)

	border += num
	next_vertex = (vertex[0] + DIR[dir][0] * num, vertex[1] + DIR[dir][1] * num)
	area += (next_vertex[0] - vertex[0]) * (next_vertex[1] + vertex[1])
	vertex = next_vertex
area = abs(area) // 2
# area = inside + border // 2 - 1
inside = area - border // 2 + 1
print(area)
print(border, inside)
print(inside + border)


