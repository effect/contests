# Time:      7  15   30
# Distance:  9  40  200
f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

time = int("".join(lines[0].split(":")[-1].strip().split()))
record = int("".join(lines[1].split(":")[-1].strip().split()))

print(time)
print(record)

num = 0
for t in range(time + 1):
	dist = t * (time - t)
	if dist > record:
		num += 1
print(num)
