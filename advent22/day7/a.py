# f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

dirpaths = {}
curdir = "/" 

for line in lines:
	# print(line)
	if line == "$ cd /":
		curdir = "/" 
		dirpaths[curdir] = 0
	elif line == "$ cd ..":
		curdir = curdir[:-1]  # remove last /
		index = curdir.rfind('/')
		curdir = curdir[:index+1]
	elif line.startswith("$ cd "):
		subdir = line.split()[-1]
		curdir += subdir + "/"
		dirpaths[curdir] = 0
	elif line == "$ ls":
		continue
	else:
		parts = line.split()
		if parts[0] == "dir":
			subdir = parts[1]
			dirpaths[curdir + subdir + "/"] = 0
		else:
			filesize = int(parts[0])
			for path in dirpaths:
				if curdir.startswith(path):
					dirpaths[path] += filesize

# print(dirpaths)

# task A
total = 0
for size in dirpaths.values():
	if size <= 100000:
		total += size
print(total)

# task B
DISK = 70000000
DF = 30000000
total = dirpaths["/"]
mindir = dirpaths["/"]
for size in dirpaths.values():
	if DISK - total + size >= DF:
		mindir = min(mindir, size)
print(mindir)