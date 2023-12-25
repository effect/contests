f = open("test.in")
f = open("input.txt")

line = ''.join([line.strip() for line in f.readlines()])

BASE = 17
MOD = 256

def hash(line):
	result = 0
	for c in line:
		result += ord(c)
		result *= BASE
		result %= MOD
	return result


result = 0
parts = line.split(',')
lenses = [[] for _ in range(MOD)]
for p in parts:
	if '=' in p:
		label, value = p.split('=')
		box = hash(label)
		for index, lense in enumerate(lenses[box]):
			if lense[0] == label:
				lenses[box][index] = (label, value)
				break
		else:
			lenses[box].append((label, value))
	if '-' in p:
		label = p[:-1]
		box = hash(label)
		for index, lense in enumerate(lenses[box]):
			if lense[0] == label:
				lenses[box].pop(index)
				break

for b in range(MOD):
	for index, lense in enumerate(lenses[b]):
		result += (1 + b) * (1 + index) * int(lense[1])

print(result)