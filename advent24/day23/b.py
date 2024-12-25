from collections import defaultdict

f = open("test.in")
f = open("input.txt")

out = open("graph.dot", "w")

lines = [line.strip() for line in f.readlines()]

adj = defaultdict(set)

out.write('graph G {\n')
for line in lines:
	a, b = line.split('-')
	adj[a].add(b)
	adj[b].add(a)

	out.write(a + ' -- ' + b + ';\n')
out.write('}\n')


vertices = list(adj.keys())
print(len(vertices))

deg = [len(adj[v]) for v in vertices]
deg = sorted(deg, reverse=True)
print(deg)

print(adj['ka'])

color = {v: -1 for v in vertices}
def dfs(v, c):
	color[v] = c
	for u in adj[v]:
		if color[u] == -1:
			dfs(u, c)

components = 0
for v in vertices:
	if color[v] == -1:
		dfs(v, components)
		components += 1

print(components)

clique = sorted(['th', 'qh', 'ww', 'sk', 'vn', 'la', 'df', 'yp', 'xp', 'kg', 'mp', 'pb', 'zk'])
print(len(clique))
print(",".join(clique))