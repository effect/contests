f = open("test.in")
f = open("input.txt")

# Y = 10
Y = 2000000

lines = [line.strip() for line in f.readlines()]

def get_coordinates(line):
	parts = line.split('=')
	c1 = parts[1].split(',')[0]
	c2 = parts[2].split(':')[0]
	c3 = parts[3].split(',')[0]
	c4 = parts[-1]
	return (int(c) for c in (c1, c2, c3, c4))

def get_radius(x1, y1, x2, y2):
	return abs(x1 - x2) + abs(y1 - y2)

def get_covered_interval(x, y, r, h):
	yd = abs(y - h)
	if yd > r:
		return None
	ir = r - yd
	return (x - ir, x + ir)  # last point included

def union_intervals(a):
	b = []
	for begin, end in sorted(a):
		if b and b[-1][1] >= begin - 1:
			b[-1][1] = max(b[-1][1], end)
		else:
			b.append([begin, end])	
	return b

def is_inside(x, intervals):
	for interval in intervals:
		if interval[0] <= x <= interval[1]:
			return True
	return False

def length(intervals):
	return sum([(a[1] - a[0] + 1) for a in intervals])

def find_intervals(h):
	intervals = []
	for i in range(N):
		xs, ys = ss[i][0], ss[i][1]
		r = rs[i]	
		interval = get_covered_interval(xs, ys, r, h)
		if interval is not None: 
			# print(interval)
			intervals.append(interval)

	# print(intervals)
	intervals = union_intervals(intervals)
	# print(intervals)
	return intervals


ss = []
bs = []
rs = []

for line in lines:
	xs, ys, xb, yb = get_coordinates(line)
	r = get_radius(xs, ys, xb, yb)

	bs.append((xb, yb)) 
	ss.append((xs, ys))
	rs.append(r)

N = len(rs)


def task_a():
	intervals = find_intervals(h=Y)
	total = length(intervals)
	print(total)

	beacons = set()
	for (xb, yb) in bs:
		if yb == Y:
			beacons.add(xb)
	print(beacons)

	for xb in beacons:
		if is_inside(xb, intervals):
			total -= 1

	print(total)


def task_b():
	MAX = 4000000
	for h in range(MAX + 1):
		intervals = find_intervals(h)
		if len(intervals) > 1:
			print(intervals)
			print(h)
			x = intervals[0][1] + 1
			y = h 
			result = x * MAX + y
			print(result)
			break	


task_a()
task_b()