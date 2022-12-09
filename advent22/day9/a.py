# f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

xh = 0
yh = 0
xt = 0
yt = 0

def sign(x):
	if x == 0: 
		return 0
	if x > 0:
		return 1
	if x < 0: 
		return -1

def head_step(xh, yh, direction):
	if direction == "R":
		xh += 1
	elif direction == "L":
		xh -= 1
	elif direction == "U":
		yh += 1
	elif direction == "D":
		yh -= 1
	return xh, yh

def tail_step(xh, yh, xt, yt):
	dx = xh - xt
	dy = yh - yt
	if abs(dx) <= 1 and abs(dy) <= 1:  # touching
		return xt, yt
	xt += sign(dx)
	yt += sign(dy)
	return xt, yt

visited = set()
visited.add((xt, yt))

for line in lines:
	direction, num = line.split()
	num = int(num)
	for i in range(num):
		xh, yh = head_step(xh, yh, direction)
		xt, yt = tail_step(xh, yh, xt, yt)
		visited.add((xt, yt))
		# print("head", xh, yh)
		# print("tail", xt, yt)
		# print()

print(len(visited))
# print(sorted(list(visited)))
