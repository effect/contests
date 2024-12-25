from collections import defaultdict

f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

adj = defaultdict(set)

for line in lines:
	a, b = line.split('-')
	adj[a].add(b)
	adj[b].add(a)


vertices = list(adj.keys())
print(len(vertices))

t1 = 0
t2 = 0
t3 = 0
for i, v in enumerate(vertices):
	if v[0] == 't':
		for a in adj[v]:
			for b in adj[a]:
				if a != v: 
					if v in adj[b]:
						if a[0] == 't' and b[0] == 't':
							t3 += 1
						elif a[0] == 't' or b[0] == 't':
							t2 += 1
						else:
							t1 += 1
print(t1, t2, t3)
result = t1 // 2 + t2 // 4 + t3 // 6
print(result)

