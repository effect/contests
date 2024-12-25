f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

keys = []
locks = []

def add(item):
	result = []
	for col in range(len(item[0])):
		num = 0
		for row in range(1, len(item) - 1):
			if item[row][col] == '#':
				num += 1
		result.append(num)
	t = keys
	if item[0][0] == '#':
		t = locks
	t.append(result)


i = 0
while i < len(lines):
	next_item = []
	while i < len(lines) and lines[i]:
		next_item.append(lines[i])		
		i += 1
	add(next_item)
	i += 1

result = 0
for lock in locks:
	for key in keys:
		for c in range(len(lock)):
			if lock[c] + key[c] > 5:
				break
		else:
			result += 1

print(result)
