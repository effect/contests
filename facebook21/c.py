
w = []
g = []
pathw = []
parent = []

def dfs(v, path_weight):
	pathw[v] = path_weight + w[v]
	for i in range(len(g)):
		if g[v][i] and pathw[i] == -1:
			parent[i] = v
			dfs(i, pathw[v])

with open("c.in") as fin, open("c.out", "w") as fout:
	T = int(fin.readline())
	for t in range(T):
		fout.write("Case #" + str(t + 1) + ": ")

		n = int(fin.readline())
		w = [int(c) for c in fin.readline().split()]
		g = [[0] * n for i in range(n)] 
		for i in range(n - 1):
			a, b = (int(c) - 1 for c in fin.readline().split())
			g[a][b] = 1
			g[b][a] = 1

		parent = [0] * n
		parent[0] = -1
		pathw = [-1] * n
		dfs(0, 0)

		max_path_weight = -1
		max_vertex = -1
		for i in range(n):
			if max_path_weight < pathw[i]:
				max_path_weight = pathw[i]
				max_vertex = i

		res = max_path_weight
		v = max_vertex
		while v > 0:
			p = parent[v]
			g[v][p] = 0
			g[p][v] = 0
			v = p

		# print("1 search: " + str(res))
		# print("1 search: " + str(pathw))
		# print("1 search leaf: " + str(max_vertex))

		w[0] = 0
		parent = [0] * n
		parent[0] = -1
		pathw = [-1] * n
		dfs(0, 0)
		res += max(pathw)		

		# print("2 search: " + str(pathw))

		fout.write(str(res))
		fout.write("\n")
