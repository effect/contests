# f = open("test.in")
f = open("input.txt")

def priority(x):
	if 'a' <= x <= 'z':
		return ord(x) - ord('a') + 1
	elif 'A' <= x <= 'Z':
		return ord(x) - ord('A') + 27

result = 0
lines = f.readlines()
for line in lines:
	n = len(line)
	a = set()
	b = set()
	for i in range(n // 2):
		a.add(line[i])
	for i in range(n // 2, n):
		b.add(line[i])
	c = a.intersection(b)
	x = c.pop()
	print(x)
	print(priority(x))
	result += priority(x)


print(result)
