# f = open("test.in")
f = open("input.txt")

def priority(x):
	if 'a' <= x <= 'z':
		return ord(x) - ord('a') + 1
	elif 'A' <= x <= 'Z':
		return ord(x) - ord('A') + 27

lines = [line.strip() for line in f.readlines()]
ngroups = len(lines) // 3
result = 0

for i in range(ngroups):
	a = set(lines[3 * i])
	b = set(lines[3 * i + 1])
	c = set(lines[3 * i + 2])
	r = a.intersection(b).intersection(c)
	x = r.pop()
	result += priority(x)

print(result)
