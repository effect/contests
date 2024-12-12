f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

def is_safe(b):
	safe = True
	for x in b:
		if not (1 <= abs(x) <= 3):
			safe = False
			break
		if x * b[0] < 0:
			safe = False
			break
	return safe


# part 1
result = 0
for line in lines:
	a = [int(x) for x in line.split()]
	b = [a[i] - a[i - 1] for i in range(1, len(a))]
	if is_safe(b):
		result += 1
print(result)

# part B
result = 0
for line in lines:
	a = [int(x) for x in line.split()]
	b = [a[i] - a[i - 1] for i in range(1, len(a))]
	if is_safe(b):
		result += 1
	else:
		if is_safe(b[1:]):
			result += 1
		elif is_safe(b[:-1]):
			result += 1
		else:
			for i in range(len(b) - 1):
				if is_safe(b[:i] + [b[i] + b[i + 1]] + b[i + 2:]):
					result += 1
					break
print(result)
