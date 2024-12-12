f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

r = set()
i = 0
while lines[i] != "":
	line = lines[i]
	a, b = line.split("|")
	r.add(b + "|" + a)
	i += 1
i += 1

def check(order):
	for a in range(len(order)):
		for b in range(a + 1, len(order)):
			if order[a] + "|" + order[b] in r:
				return False
	return True

# part 1
start = i
result = 0
while i < len(lines):
	order = lines[i].split(",")
	if check(order):
		result += int(order[len(order) // 2])
	i += 1
print(result)


# part 2
def reorder(order):
	for a in range(len(order)):
		for b in range(a + 1, len(order)):
			if order[a] + "|" + order[b] in r:
				order[a], order[b] = order[b], order[a]
	return order

i = start
result = 0
while i < len(lines):
	order = lines[i].split(",")
	if not check(order):
		order = reorder(order)
		result += int(order[len(order) // 2])
	i += 1
print(result)