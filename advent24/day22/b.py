from collections import defaultdict

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

d = [[0] * STEPS for _ in range(len(a))]
p = [[0] * STEPS for _ in range(len(a))]

for i, x in enumerate(a):
	for it in range(STEPS):
		nx = transform(x)
		p[i][it] = (nx % 10)
		d[i][it] = (nx % 10) - (x % 10)
		x = nx

total = defaultdict(int)
for ind, seq in enumerate(d):
	cur = set()
	for i in range(len(seq) - 3):
		quad = (seq[i], seq[i + 1], seq[i + 2], seq[i + 3])
		if quad in cur: 
			continue
		else:
			cur.add(quad)
			total[quad] += p[ind][i + 3]

print(max(total.values()))
