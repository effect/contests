import time
TLE = 100

f = open("test.in")
f = open("input.txt")

TIME = 24

lines = [line.strip() for line in f.readlines()]

NAMES = ["ore", "clay", "obsidian", "geode"]
COSTS = "costs "

geodes = 0
earliest_geode_robot = TIME + 1
last_time = time.time()

def parse_blueprint(line):
	# Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
	line = line.strip('.').split(': ')[-1]
	descriptions = line.split(". ")
	cost = [[0], [0], [0] * 2, [0] * 3]
	for i, description in enumerate(descriptions):
		ic = description.index(COSTS)
		desc = description[ic + len(COSTS):]
		descs = desc.split(" and ")
		for d in descs:
			num, rtype = d.split()
			cost[i][NAMES.index(rtype)] = int(num)
	return cost

visited = set()

def sim(cost, minutes, resources, robots):
	state = tuple([minutes] + resources + robots)
	if state in visited:
		return
	visited.add(state)

	actual_time = time.time()
	global last_time
	if actual_time - last_time > TLE:
		return

	if minutes > TIME:
		global geodes
		if geodes < resources[-1]:
			geodes = resources[-1]
			print(geodes)
			print(resources)
			print(robots)
			last_time = time.time()
		return

	# increase resources produced by existing robots
	next_resources = resources.copy()
	for i, r in enumerate(robots):
		next_resources[i] += r

	# try build each type of robot, start with more advanced
	for i in range(3, -1, -1):  
		for j, req in enumerate(cost[i]):
			if resources[j] < req:
				break
		else:
			# all requirements satisfied, can build new robot of type i
			if i == 0 and robots[i] >= 4:
				continue  # we don't want too many ore robots
			
			next_robots = robots.copy()
			next_robots[i] += 1

			robot_next_resources = next_resources.copy()
			for j, req in enumerate(cost[i]):
				robot_next_resources[j] -= req
			sim(cost, minutes + 1, robot_next_resources, next_robots)
			if i == 2:  # if it's possible to build geode or obs robot, then do any of them
				break
	
	# try without building new robots
	sim(cost, minutes + 1, next_resources, robots)

result = 0
for index, line in enumerate(lines):
	cost = parse_blueprint(line)
	print(cost)

	geodes = 0
	visited = set()
	last_time = time.time()
	sim(cost, 1, [0] * 4, [1, 0, 0, 0])
	print(geodes)
	print()
	result += geodes * (index + 1)

print(result)