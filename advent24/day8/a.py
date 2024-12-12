f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]
rows = len(lines)
cols = len(lines[0])

pos = set()

for ai in range(rows):
	for aj in range(cols):
		if lines[ai][aj] != '.':
			for bi in range(rows):
				for bj in range(cols):
					if (ai == bi) and (aj == bj):
						continue
					if lines[bi][bj] == lines[ai][aj]:
						di = ai - bi
						dj = aj - bj						

						# for k in range(1, 2):  # task 1
						
						for k in range(rows + cols):	# task 2
							ni = ai + k * di
							nj = aj + k * dj
							if (0 <= ni < rows) and (0 <= nj < cols):
								pos.add((ni, nj))
							else:
								break

print(len(pos))