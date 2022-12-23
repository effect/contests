from collections import Counter

# f = open("tinytest.in")
# f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

ROUNDS = 10  # task a
ROUNDS = 10000  # task b

# coord format: (row_number, column_number)
adj_free = [
	[(-1, -1), (-1, 0), (-1, 1)], 
	[(1, -1), (1, 0), (1, 1)], 
	[(-1, -1), (0, -1), (1, -1)], 
	[(-1, 1), (0, 1), (1, 1)], 
]

def get_positions(lines):
	positions = set()
	for rn, row in enumerate(lines):
		for cn, sym in enumerate(row):
			if sym == '#':
				positions.add((rn, cn))
	return positions

		
def get_next_position(position, positions):
	num_free_sides = 4
	last_free_side = -1
	for i in reversed(range(4)):
		side = (i + direction) % 4
		for delta in adj_free[side]:
			adj_position = (position[0] + delta[0], position[1] + delta[1])
			if adj_position in positions:
				num_free_sides -= 1
				break
		else:
			last_free_side = side

	if num_free_sides == 4 or num_free_sides == 0:
		return position
	return (position[0] + adj_free[last_free_side][1][0], position[1] + adj_free[last_free_side][1][1])


def propose_positions(positions):
	next_positions = dict()
	for position in positions:
		next_positions[position] = get_next_position(position, positions)
	return next_positions


def draw_positions(positions):
	min_row = min([position[0] for position in positions])
	max_row = max([position[0] for position in positions])
	min_col = min([position[1] for position in positions])
	max_col = max([position[1] for position in positions])
	lines = ['.' * (max_col - min_col + 1) for _ in range(max_row - min_row + 1)]
	for position in positions:
		rown = position[0] - min_row
		coln = position[1] - min_col
		lines[rown] = lines[rown][:coln] + '#' + lines[rown][coln + 1:]
	print("\n".join(lines))


positions = get_positions(lines)
direction = 0

# print("Initial state: ")
# draw_positions(positions)
# print(positions)

for round in range(ROUNDS):
	proposed_positions = propose_positions(positions)
	# print(f"Round {round + 1}:")
	# print("Proposed positions: ")
	# draw_positions(proposed_positions.values())
	counter = Counter(proposed_positions.values())
	next_positions = set()
	cnt_moved = 0
	for current_position, proposed_position in proposed_positions.items():
		if counter[proposed_position] == 1:
			next_positions.add(proposed_position)
			if proposed_position != current_position:
				cnt_moved += 1
		else:
			next_positions.add(current_position)

	positions = next_positions
	direction = (direction + 1) % 4
	# print(f"After round {round + 1}:")
	# draw_positions(positions)

	if cnt_moved == 0:
		print(f"No moves on round {round + 1}")
		break

# draw_positions(positions)

min_row = min([position[0] for position in positions])
max_row = max([position[0] for position in positions])
min_col = min([position[1] for position in positions])
max_col = max([position[1] for position in positions])
print(min_row, max_row, min_col, max_col)
print( (max_row - min_row + 1) * (max_col - min_col + 1) - len(positions) )