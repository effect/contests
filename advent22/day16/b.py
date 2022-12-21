f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

INF = 1000000
START_VERTEX = 'AA'
TIME = 26

flow_by_name = dict()
adjacent_by_name = dict()


# Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
def parse_line(line):
	parts = line.split()
	vertex_name = parts[1]
	rate = int(parts[4].split('=')[1].strip(';'))
	flow_by_name[vertex_name] = rate
	to = [name.strip(',') for name in parts[9:]]
	adjacent_by_name[vertex_name] = to

def inf_dist():
	return {name : INF for name in adjacent_by_name.keys()}

def calc_dist():
	# init
	verticies = adjacent_by_name.keys()
	dist = {name : inf_dist() for name in verticies}  # vertex_name -> vertex_name -> dist
	for v, adjacent in adjacent_by_name.items():
		for adjv in adjacent:
			dist[v][adjv] = 1

	# floyd
	for vk in verticies:
		for vi in verticies:
			for vj in verticies:
				dist[vi][vj] = min(dist[vi][vj], dist[vi][vk] + dist[vk][vj])
	return dist

def get_verticies_with_flow():
	verticies = [START_VERTEX]
	for name, flow in flow_by_name.items():
		if flow > 0:
			verticies.append(name)
	return verticies

def compress_graph(fv):
	n = len(fv)  # number of verticies in compressed graph
	a = [[0] * n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			a[i][j] = dist[fv[i]][fv[j]] + 1  # +1 to account for time needed to release gas
	return n, a 


for line in lines:
	parse_line(line)

dist = calc_dist()
# print(flow_by_name)
# print(adjacent_by_name)
# print(dist)

fv = get_verticies_with_flow()
n, a = compress_graph(fv)
flow_by_index = [flow_by_name[name] for name in fv]
print(fv)
print(n)
print(a)
print(flow_by_index)

iterations = 0
max_points = 0
max_combination = set()

def gen(vertex, available, time_left, points):
	global iterations
	global max_points
	global max_combination
	iterations += 1
	if iterations % 100000 == 0:
		print(iterations, max_points)  # it took ~3e9 iterations to get correct result
	if max_points < points:
		max_points = points
		max_combination = available.copy()

	for which_move in range(2):
		# which_move = time_left[1] >= time_left[0]  # who will extend his path
		cur_vertex = vertex[which_move]
		cur_time_left = time_left[which_move]

		for v in available.copy():
			if a[cur_vertex][v] <= cur_time_left:
				available.remove(v)
				next_vertex = (vertex[0], v) if which_move else (v, vertex[1])
				next_time = (time_left[0], time_left[1] - a[cur_vertex][v]) if which_move else (time_left[0] - a[cur_vertex][v], time_left[1])
				next_points = points + (time_left[which_move] - a[cur_vertex][v]) * flow_by_index[v]
				gen(next_vertex, available, next_time, next_points)
				available.add(v)


gen((0, 0), set(range(1, n)), (TIME, TIME), 0)
print(iterations)
print(max_points)
print(set(range(1, n)) - max_combination)	
