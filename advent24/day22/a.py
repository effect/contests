f = open("test.in")
f = open("input.txt")

STEPS = 2000
MOD = 16777216

a = [int(line.strip()) for line in f.readlines()]

def transform(x):
	x = ((x * 64) ^ x) % MOD
	x = ((x // 32) ^ x) % MOD
	x = ((x * 2048) ^ x) % MOD
	return x

result = 0
for x in a:
	print(x)
	for it in range(STEPS):
		x = transform(x)
	result += x
print(result)
