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
for p in parts:
	result += hash(p)
print(result)