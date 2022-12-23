f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

INF = 1000000
START_VERTEX = 'AA'
TIME = 30

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
			a[i][j] = dist[fv[i]][fv[j]]
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

d = [[[-INF] * (1 << n) for i in range(n)] for j in range(TIME+1)]
d[0][0][0] = 0
for t in range(1, TIME+1):
	print(t)
	for v in range(n):
		# come from another vertex to v
		for v2 in range(n):
			pt = t - a[v][v2]
			if pt >= 0:
				for released in range(1 << n):
					d[t][v][released] = max(d[t][v][released], d[pt][v2][released])
		# release gas in v
		if t > 0:
			for released in range(1 << n):
				if released & (1 << v):
					d[t][v][released] = d[t - 1][v][released ^ (1 << v)] + (TIME - t) * flow_by_index[v]

max_released = 0
for v in range(n):
	max_released = max(max_released, max(d[TIME][v]))
print(max_released)

for v in range(n):
	if max_released in d[TIME][v]:
		print(v, format(d[TIME][v].index(max_released), '016b'))

