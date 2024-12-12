f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

rows = len(lines)
cols = len(lines[0])

# part 1
d = ((1, 0), (-1, 0),  
		 (0, 1), (0, -1), 
		 (1, 1), (-1, -1), 
		 (1, -1), (-1, 1))

XMAS = "XMAS"
result = 0
for i in range(rows):
	for j in range(cols):
		for dir in range(len(d)):
			w = ""
			for k in range(4):
				ci = i + d[dir][0] * k
				cj = j + d[dir][1] * k
				if not ((0 <= ci < rows) and (0 <= cj < cols)):
					break
				w += lines[ci][cj]
			if w == XMAS:
				result += 1
print(result)

# part 2
d = ( ((-1, -1), (1, 1)), 
			((-1, 1), (1, -1)), 
		)
result = 0
for i in range(1, rows - 1):
	for j in range(1, cols - 1):
		if lines[i][j] == "A":
			nms = 0
			for dir in range(len(d)):
				nm = 0
				ns = 0
				for k in range(len(d[dir])):
					ci = i + d[dir][k][0]
					cj = j + d[dir][k][1]
					if lines[ci][cj] == "M":
						nm += 1
					if lines[ci][cj] == "S":
						ns += 1
				if nm == 1 and ns == 1:
					nms += 1
			if nms == 2:
				result += 1
print(result)