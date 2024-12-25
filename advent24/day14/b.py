f = open("test.in")
f = open("input.txt")

ROWS = 7
COLS = 11
ROWS = 103
COLS = 101

STEPS = 100

lines = [line.strip() for line in f.readlines()]
n = len(lines)

def get_numbers(part):
	part = part[2:]
	x, y = part.split(",")
	return int(x), int(y)

x0 = [0] * n
y0 = [0] * n
vx = [0] * n
vy = [0] * n

for i, line in enumerate(lines):
	p, v = line.split()
	x0[i], y0[i] = get_numbers(p)
	vx[i], vy[i] = get_numbers(v)

for it in range(10000):
	if it % 5000 == 0:
		print(it)
	a = [[0] * COLS for _ in range(ROWS)]
	qUL = qUR = qDL = qDR = 0
	ta = tb = 0
	for i in range(n):
		x = (x0[i] + it * vx[i]) % COLS
		y = (y0[i] + it * vy[i]) % ROWS
		a[y][x] += 1
		if a[y][x] == 1:
			if (x < COLS // 2) and (y < ROWS // 2):
				qUL += 1
			if (x > COLS // 2) and (y < ROWS // 2):
				qUR += 1
			if (x < COLS // 2) and (y > ROWS // 2):
				qDL += 1
			if (x > COLS // 2) and (y > ROWS // 2):
				qDR += 1
			if (x + y < COLS // 2):
				ta += 1
			if (x - y > COLS // 2):
				tb += 1


	# if abs(qUL - qUR) < 50 and abs(qDL - qDR) < 50 and ((qUL + qUR) * 1.25 < (qDL + qDR)):
	if ta < 35 and tb < 35:
		print(qUL, qUR, qDL, qDR, n // 4)
		print(ta, tb)
		print(it)
		for i in range(ROWS):
			for j in range(COLS):
				if a[i][j]:
					print('#', end='')
				else:
					print(' ', end='')
			print()
		print()

# print(qUL * qUR * qDL * qDR)