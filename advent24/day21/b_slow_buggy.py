import numpy as np

f = open("test.in")
# f = open("input.txt")

INF = 99
ACT = 9

numeric = [
	[ '7', '8', '9'], 
	[ '4', '5', '6'], 
	[ '1', '2', '3'], 
	[INF,  '0', 'A'], 
]

direct = [
	[INF, 			(-1, 0), ACT], 
	[(0, -1),   ( 1, 0), (0, 1)], 
]

symbol = {
	(-1, 0): '^', 
	ACT: 'A', 
	(0, -1): '<', 
	(1, 0): 'v', 
	(0, 1): '>', 
}

def build_reverese_index(keypad):
	index = dict()
	for i in range(len(keypad)):
		for j in range(len(keypad[i])):
			index[keypad[i][j]] = (i, j)
	return index

numeric_index = build_reverese_index(numeric)
directional_index = build_reverese_index(direct)

lines = [line.strip() for line in f.readlines()]

def gen_numeric_paths(line_to_type, position, path):
	if len(line_to_type) == 0:
		yield path
		return
	i, j = numeric_index[position]
	char = line_to_type[0]
	to_i, to_j = numeric_index[char]
	di, dj = to_i - i, to_j - j
	step_i, step_j = np.sign(di), np.sign(dj)
	if step_i == 0 and step_j == 0:
		next_path = path[:]
		next_path.append(ACT)
		yield from gen_numeric_paths(line_to_type[1:], position, next_path)
	elif step_i == 0 or step_j == 0:
		next_path = path[:]
		next_path.append((step_i, step_j))
		next_i, next_j = i + step_i, j + step_j
		next_position = numeric[next_i][next_j]
		if next_position != INF:
			yield from gen_numeric_paths(line_to_type, next_position, next_path)
	else:
		# 2 options
		tmp = step_i
		step_i = 0
		next_path = path[:]
		next_path.append((step_i, step_j))
		next_i, next_j = i + step_i, j + step_j
		next_position = numeric[next_i][next_j]
		if next_position != INF:
			yield from gen_numeric_paths(line_to_type, next_position, next_path)

		step_i = tmp
		step_j = 0
		next_path = path[:]
		next_path.append((step_i, step_j))
		next_i, next_j = i + step_i, j + step_j
		next_position = numeric[next_i][next_j]
		if next_position != INF:
			yield from gen_numeric_paths(line_to_type, next_position, next_path)


def gen_directional_paths(to_type, position, path):
	if len(to_type) == 0:
		yield path
		return 
	i, j = directional_index[position]
	char = to_type[0]
	to_i, to_j = directional_index[char]
	di, dj = to_i - i, to_j - j
	step_i, step_j = np.sign(di), np.sign(dj)
	if step_i == 0 and step_j == 0:
		next_path = path[:]
		next_path.append(ACT)
		yield from gen_directional_paths(to_type[1:], position, next_path)
	elif step_i == 0 or step_j == 0:
		next_path = path[:]
		next_path.append((step_i, step_j))
		next_i, next_j = i + step_i, j + step_j
		next_position = direct[next_i][next_j]
		if next_position != INF:
			yield from gen_directional_paths(to_type, next_position, next_path)
	else:
		# 2 options
		tmp = step_i
		step_i = 0
		next_path = path[:]
		next_path.append((step_i, step_j))
		next_i, next_j = i + step_i, j + step_j
		next_position = direct[next_i][next_j]
		if next_position != INF:
			yield from gen_directional_paths(to_type, next_position, next_path)

		step_i = tmp
		step_j = 0
		next_path = path[:]
		next_path.append((step_i, step_j))
		next_i, next_j = i + step_i, j + step_j
		next_position = direct[next_i][next_j]
		if next_position != INF:
			yield from gen_directional_paths(to_type, next_position, next_path)



def keep_shortest_paths(paths):
	min_len = min([len(path) for path in paths])
	return [path for path in paths if len(path) == min_len]

def visualize(path):
	return "".join(symbol[p] for p in path)

def get_number(line):
	return int(line[:-1])

def get_length(paths):
	return len(paths[0])

'''
best_guess = {
	(ACT, (1, 0)): [(-1, 0), (0, -1)], 
	(ACT, (0, -1)): [(-1, 0), (0, -1), (0, -1)],
	((-1, 0), (0, 1)): [(0, 1), (1, 0)], 
	((0, 1), (-1, 0)): [(-1, 0), (0, -1)],
	((1, 0), ACT): [(0, 1), (-1, 0)], 
	((0, -1), ACT): [(0, 1), (0, 1), (-1, 0)], 
	((0, -1), (-1, 0)): [(0, 1), (-1, 0)], 
	((-1, 0), (0, -1)): [(-1, 0), (0, -1)],   
}'''
best_guess = {
	# (ACT, (1, 0)): [(-1, 0), (0, -1)], 
	(ACT, (1, 0)): [(0, -1), (-1, 0)], 	

	(ACT, (0, -1)): [(1, 0), (0, -1), (0, -1)],
	# (ACT, (0, -1)): [(0, -1), (-1, 0), (0, -1)],

	# ((-1, 0), (0, 1)): [(0, 1), (1, 0)], 
	((-1, 0), (0, 1)): [(1, 0), (0, 1)], 

	# ((0, 1), (-1, 0)): [(-1, 0), (0, -1)],
	((0, 1), (-1, 0)): [(0, -1), (-1, 0)],

	# ((1, 0), ACT): [(0, 1), (-1, 0)], 
	((1, 0), ACT): [(-1, 0), (0, 1)], 

	((0, -1), ACT): [(0, 1), (0, 1), (-1, 0)], 
	# ((0, -1), ACT): [(0, 1), (-1, 0), (0, 1)], 

	((0, -1), (-1, 0)): [(0, 1), (-1, 0)],    # 100%
	((-1, 0), (0, -1)): [(1, 0), (0, -1)],    # 100%
}


def trajectory(position_start, position_end):
	if position_start == position_end:
		return []
	tr = []
	i, j = directional_index[position_start]
	to_i, to_j = directional_index[position_end]
	di, dj = to_i - i, to_j - j
	step_i, step_j = np.sign(di), np.sign(dj)
	if di == 0 or dj == 0:
		while not ((i == to_i) and (j == to_j)):
			i += step_i
			j += step_j
			tr.append((step_i, step_j))
	else:
		tr = best_guess[(position_start, position_end)]
	return tr


def shortest_path(to_type):
	position = ACT
	result = []
	for next_position in to_type:
		result.extend(trajectory(position, next_position))
		print(f"trajectory from {position} to {next_position}: {trajectory(position, next_position)}")
		result.append(ACT)
		position = next_position
	print("total path: ", result)
	return result


def gen_levels(line):
	paths_0 = [path for path in gen_numeric_paths(line, 'A', [])]
	paths_0 = keep_shortest_paths(paths_0)
	min_length = 9999
	candidates = []
	for path in paths_0:
		print(visualize(path))
		next_paths = [path for path in gen_directional_paths(path, ACT, [])]
		next_paths = keep_shortest_paths(next_paths)
		cur_len = get_length(next_paths)
		if cur_len < min_length:
			min_length = cur_len
			candidates = next_paths
		elif cur_len == min_length:
			candidates.extend(next_paths)

	print("Finished paths_1")
	print(min_length)
	# print(candidates)
	paths_1 = candidates

	min_length = 9999
	candidates = []
	for path in paths_1:
		# print(visualize(path))
		next_paths = [path for path in gen_directional_paths(path, ACT, [])]
		next_paths = keep_shortest_paths(next_paths)
		cur_len = get_length(next_paths)
		if cur_len < min_length:
			min_length = cur_len
			candidates = next_paths
		elif cur_len == min_length:
			candidates.extend(next_paths)

	print("Finished paths_2")
	print(min_length)
	# print(candidates)
	paths_2 = candidates

	return min_length


def gen_euristic_levels(line):
	paths_0 = [path for path in gen_numeric_paths(line, 'A', [])]
	paths_0 = keep_shortest_paths(paths_0)
	min_length = 9999
	for path in paths_0:
		print(visualize(path))
		p = path
		for it in range(2):
			print(it, len(p))
			p = shortest_path(p)
			print(visualize(p))
		min_length = min(min_length, len(p))
	return min_length


result = 0
for line in lines:
	print()
	# length = gen_levels(line)
	length = gen_euristic_levels(line)
	print(length, get_number(line))
	result += length * get_number(line)
print(result)