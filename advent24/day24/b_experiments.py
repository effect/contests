from collections import Counter, defaultdict

f = open("test.in")
f = open("input.txt")
out = open("graph.dot", "w")
out.write("digraph G {\n")

lines = [line.strip() for line in f.readlines()]

variables = dict()
expressions = dict()
forward = defaultdict(list)

vars_list = []

for line in lines:
	if ':' in line:
		var, value = (part.strip() for part in line.split(':'))
		variables[var] = int(value)
	elif '->' in line:
		expr, res = (part.strip() for part in line.split('->'))
		a, op, b = expr.split()
		expressions[res] = (a, op, b)

		forward[a].append(res)
		forward[b].append(res)

		# x00 AND y00 -> z00
		out.write(a + " -> " + res + ";\n")
		out.write(b + " -> " + res + ";\n")

# 		if (a[0] in ('x', 'y')) or (b[0] in ('x', 'y')):
# 			if a[0] != 'x':
# 				a, b = b, a
# 			vars_list.append((a, op, b))
# vars_list = sorted(vars_list)
# print(len(vars_list))
# for i in range(0, len(vars_list), 2):
# 	print(vars_list[i], vars_list[i + 1])
		
out.write('}')

print(len(variables))
print(len(expressions))

def calc(var):
	if var in variables:
		return variables[var]
	(a, op, b) = expressions[var]
	av = calc(a)
	bv = calc(b)
	if op == 'AND':
		result = av and bv
	if op == 'OR':
		result = av or bv
	if op == 'XOR':
		result = av ^ bv
	variables[var] = result
	return result


def get_sources(node):
	if node[0] in ('x', 'y'):
		return [int(node[1:])]
	(a, op, b) = expressions[node]
	ra = get_sources(a)
	rb = get_sources(b)
	return ra + rb


def reverse_path(node):
	if node[0] in ('x', 'y'):
		return set([node])
	(a, op, b) = expressions[node]
	ra = reverse_path(a)
	rb = reverse_path(b)
	cur = set([node]) if node[0] != 'z' else set()
	return cur | ra | rb


def forward_path(node):
	if node[0] == 'z':
		return set([node])
	result = set()
	if not (node[0] in ('x', 'y')):
		result.add(node)
	for next in forward[node]:
		result |= forward_path(next)
	return result


NB = 46
rev = [0] * NB
forw = [0] * NB

for ind in range(NB):
	varz = 'z' + str(ind).zfill(2)
	src = set(get_sources(varz))
	rev[ind] = reverse_path(varz)

	varx = 'x' + str(ind).zfill(2)
	forw[ind] = forward_path(varx)
	# print(var, src, rev[ind])

print('***\n' * 3)
print(forw[0])
for ind in range(NB):
	if ('z' + str(ind).zfill(2) not in forw[0]):
		print(ind)
for ind in range(NB):
	if ('z' + str(ind).zfill(2) not in forw[ind]):
		print(ind)
	if ('x' + str(ind).zfill(2) not in rev[ind]):
		print(ind)

print("START")

ind = 0
cur_rev = rev[ind]
print(ind, len(cur_rev))

for ind in range(1, NB):
	prev_rev = rev[ind - 1]
	cur_rev = rev[ind]

	prev_forw = forw[ind - 1]
	cur_forw = forw[ind]
	print(ind, "reverse from Z", len(cur_rev), len(cur_rev) - len(prev_rev))
	print(ind, "forward from X", len(cur_forw), len(prev_forw) - len(cur_forw))
	if not (prev_rev <= cur_rev):
		print("rev diff")
		print(ind, prev_rev - cur_rev)
	# if not (cur_forw <= prev_forw):
	print("forw diff (cur - prev)", ind, cur_forw - prev_forw)	
	print("forw diff (prev - cur)", ind, prev_forw - cur_forw)
