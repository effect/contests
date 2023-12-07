# Time:      7  15   30
# Distance:  9  40  200
f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

times = [int(a) for a in lines[0].split(":")[-1].strip().split()]
records = [int(a) for a in lines[1].split(":")[-1].strip().split()]

result = 1
for i in range(len(times)):
	time = times[i]
	record = records[i]
	num = 0
	for t in range(time + 1):
		dist = t * (time - t)
		if dist > record:
			num += 1
	print(num)
	result *= num
print(result)