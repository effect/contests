f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

def calc(a):
	if len(a) == 1:
		yield a[0]
	else:
		yield from calc([a[0] + a[1]] + a[2:])
		yield from calc([a[0] * a[1]] + a[2:])
		# just for task 2
		yield from calc([int(str(a[0]) + str(a[1]))] + a[2:])


result = 0
for line in lines:
	res, a = line.split(":")
	res = int(res)
	a = [int(x) for x in a.strip().split()]
	
	for r in calc(a):
		if r == res:
			result += res
			break

print(result)

