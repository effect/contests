from collections import defaultdict
f = open("test.in")
f = open("input.txt")
lines = [line.strip() for line in f.readlines()]

# f = open("input.graph", "w")
graph = defaultdict(list)

# based on GraphViz visualization (neato mode)
edges_to_remove = (
	('zgp', 'cgt'), 
	('bcf', 'fxk'), 
	('xhl', 'shj'), 
)

for line in lines:
	l, r = line.split(": ")
	adj = r.split(" ")
	for node in adj:
		if (l, node) in edges_to_remove or (node, l) in edges_to_remove:
			print(l, node)
			continue
		graph[l].append(node)
		graph[node].append(l)

# print(graph)
num_vertices = len(graph)
print(num_vertices)

visited = {v: False for v in graph.keys()}

def dfs(v):
	visited[v] = True
	for node in graph[v]:
		if not visited[node]:
			dfs(node)

dfs('zgp')
num_visited = sum(visited.values())
print(num_visited)
print(num_visited * (num_vertices - num_visited))
