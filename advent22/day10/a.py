# f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

CYCLE = 40

total = 0
value = 1
time = 0
next_cycle = CYCLE // 2

for line in lines:
	delta = 0
	if line == "noop":
		time += 1
	else:
		time += 2
		delta = int(line.split()[-1])

	if time >= next_cycle:
		# print(time, next_cycle, value)
		# print(next_cycle * value)
		total += next_cycle * value
		next_cycle += CYCLE

	value += delta
	if time > 220:
		break

print(total)
