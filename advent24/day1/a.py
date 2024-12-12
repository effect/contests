f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]
a = [int(pair.split()[0]) for pair in lines]
b = [int(pair.split()[1]) for pair in lines]
a = sorted(a)
b = sorted(b)

# part 1
result = 0
for x, y in zip(a, b):
	result += abs(x - y)
print(result)

# part 2
result = 0
for x in a:
	result += x * b.count(x)
print(result)