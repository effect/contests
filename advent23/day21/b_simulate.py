ITERATIONS = 1200
D = ((0, 1), (0, -1), (-1, 0), (1, 0))

f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]
n = len(lines)
# print(n, len(lines[0]))


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
		# if 0 <= tr < n and 0 <= tc < n:
		result.append((tr, tc))
	return result


f = open('num.out', 'w')
rs, cs = get_start()
lines[rs] = lines[rs].replace('S', '.')
wave = {(rs, cs)}
wave_all = {(rs, cs)}
for iteration in range(ITERATIONS):
	next_wave = set()
	next_wave_all = set()
	for r, c in wave:
		next = get_next(r, c)
		for nr, nc in next:
			if lines[nr % n][nc % n] == '.':
				next_wave.add((nr, nc))
			next_wave_all.add((nr, nc))
	wave = next_wave
	wave_all = next_wave_all
	if (iteration + 1) % 50 == 0:
		print((iteration + 1), len(wave))
		print((iteration + 1), len(wave_all))
	f.write('num: ' + str(iteration + 1) + ' ' +  str(len(wave)) + '\n')
	f.write('all: ' + str(iteration + 1) + ' ' +  str(len(wave_all)) + '\n')