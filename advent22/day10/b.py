# f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

CYCLE = 40

total = 0
value = 1
time = 0

screen = ["."] * CYCLE * 6

for line in lines:
	delta = 0
	if line == "noop":
		next_time = time + 1
	else:
		next_time = time + 2
		delta = int(line.split()[-1])

	for i in range(time, next_time):
		if value - 1 <= i % CYCLE <= value + 1:
			screen[i] = "#"

	value += delta
	time = next_time
	# print("".join(screen))

for i in range(6):
	print("".join(screen[i * CYCLE : (i + 1) * CYCLE]))