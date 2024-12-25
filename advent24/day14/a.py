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


qUL = qUR = qDL = qDR = 0
for i in range(n):
	x = (x0[i] + STEPS * vx[i]) % COLS
	y = (y0[i] + STEPS * vy[i]) % ROWS
	if (x < COLS // 2) and (y < ROWS // 2):
		qUL += 1
	if (x > COLS // 2) and (y < ROWS // 2):
		qUR += 1
	if (x < COLS // 2) and (y > ROWS // 2):
		qDL += 1
	if (x > COLS // 2) and (y > ROWS // 2):
		qDR += 1
print(qUL * qUR * qDL * qDR)