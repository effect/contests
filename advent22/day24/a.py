f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]
NR = len(lines)
NC = len(lines[0])
MAX_TIME = 10000

print(NR, NC)

adj_delta = [ (0, 0), (0, 1), (0, -1), (1, 0), (-1, 0) ]


def is_start(cell, forward=True):
	if forward:
		return cell == (0, 1)
	return is_final(cell)

def is_final(cell, forward=True):
	if forward:
		return cell == (NR - 1, NC - 2)
	return is_start(cell)

def is_inside(cell):
	return (0 < cell[0] < NR - 1) and (0 < cell[1] < NC - 1)

def is_row_position_free(row, col, time):
	pos_adj_r = (col - 1 - time) % (NC - 2) + 1
	pos_adj_l = (col - 1 + time) % (NC  -2) + 1
	return (pos_adj_l not in go_left[row]) and (pos_adj_r not in go_right[row])

def is_column_position_free(row, col, time):
	pos_adj_u = (row - 1 + time) % (NR - 2) + 1
	pos_adj_d = (row - 1 - time) % (NR - 2) + 1
	return (pos_adj_u not in go_up[col]) and (pos_adj_d not in go_down[col])

def is_free(nr, nc, time):
	return is_row_position_free(nr, nc, time) and is_column_position_free(nr, nc, time)

def parse_blizzard(lines, NR, NC):
	go_left = [set() for _ in range(NR)]
	go_right = [set() for _ in range(NR)]
	go_up = [set() for _ in range(NC)]
	go_down = [set() for _ in range(NC)]

	for rn in range(1, NR - 1):
		for cn in range(1, NC - 1):
			if lines[rn][cn] == '>':
				go_right[rn].add(cn)
			elif lines[rn][cn] == '<':
				go_left[rn].add(cn)
			elif lines[rn][cn] == '^':
				go_up[cn].add(rn)
			elif lines[rn][cn] == 'v':
				go_down[cn].add(rn)

	return go_left, go_right, go_up, go_down


def find_finish(start_time, forward):
	q = set()
	start = (0, 1) if forward else (NR - 1, NC - 2)
	q.add(start)	

	for time in range(start_time, MAX_TIME):
		# print(time, q)
		next_wave = set()
		while len(q) > 0:
			cell = q.pop()

			for delta in adj_delta:
				next_cell = (cell[0] + delta[0], cell[1] + delta[1])
				if is_final(next_cell, forward):
					return time

				if is_start(next_cell, forward) or (is_inside(next_cell) and is_free(next_cell[0], next_cell[1], time)):
					next_wave.add(next_cell)
		q = next_wave


go_left, go_right, go_up, go_down = parse_blizzard(lines, NR, NC)
time = find_finish(1, True)
print(time)
time = find_finish(time, False)
print(time)
time = find_finish(time, True)
print(time)