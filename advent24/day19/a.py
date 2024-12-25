f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

words = [part.strip() for part in lines[0].split(',')]
lines = lines[2:]

result = 0
for line in lines:
	n = len(line)
	d = [0] * (n + 1)
	d[0] = 1
	for i in range(n):
		if d[i]:
			for w in words:
				if i + len(w) <= n and line[i:i+len(w)] == w:
					# d[i + len(w)] = 1  # part 1
					d[i + len(w)] += d[i]  # part 2 
	if d[n]:
		result += d[n]
print(result)
