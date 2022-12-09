# f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

N = 10
x = [0] * N
y = [0] * N 

def sign(x):
	if x == 0: 
		return 0
	if x > 0:
		return 1
	if x < 0: 
		return -1

def head_step(x, y, direction):
	if direction == "R":
		x[0] += 1
	elif direction == "L":
		x[0] -= 1
	elif direction == "U":
		y[0] += 1
	elif direction == "D":
		y[0] -= 1

def tail_step(x, y, j):
	xh = x[j-1]
	yh = y[j-1]
	xt = x[j]
	yt = y[j]

	dx = xh - xt
	dy = yh - yt
	if abs(dx) <= 1 and abs(dy) <= 1:  # touching
		return 
	xt += sign(dx)
	yt += sign(dy)
	x[j] = xt
	y[j] = yt


visited = set()
visited.add((0, 0))

for line in lines:
	direction, num = line.split()
	num = int(num)
	for i in range(num):
		head_step(x, y, direction)
		for j in range(1, N):
			tail_step(x, y, j)

		visited.add((x[N-1], y[N-1]))

print(len(visited))
# print(sorted(list(visited)))
