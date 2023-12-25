ITERATIONS = 64
D = ((0, 1), (0, -1), (-1, 0), (1, 0))

f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]
n = len(lines)
print(n, len(lines[0]))


def get_start():
	for i in range(n):
		for j in range(n):
			if lines[i][j] == 'S':
				return i, j


def get_next(r, c):
	result = []
	for dr, dc in D:
		tr = r + dr
		tc = c + dc
		if 0 <= tr < n and 0 <= tc < n:
			result.append((tr, tc))
	return result


rs, cs = get_start()
lines[rs] = lines[rs].replace('S', '.')
wave = {(rs, cs)}
for iteration in range(ITERATIONS):
	next_wave = set()
	for r, c in wave:
		next = get_next(r, c)
		for nr, nc in next:
			if lines[nr][nc] == '.':
				next_wave.add((nr, nc))
	wave = next_wave
print(len(wave))