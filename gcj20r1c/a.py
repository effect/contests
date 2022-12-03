import sys

fin = sys.stdin
fout = sys.stdout

nt = int(fin.readline())

for tn in range(nt):
  fout.write("Case #" + str(tn + 1) + ": ")

  x, y, s = fin.readline().split()
  x = int(x)
  y = int(y)

  result = "IMPOSSIBLE"

  for time in range(len(s) + 1):
  	steps = abs(x) + abs(y)
  	if steps <= time:
  		result = time
  		break
  	
  	if time < len(s):
	  	c = s[time]
	  	if c == "N":
	  		y += 1
	  	if c == "S":
	  		y -= 1
	  	if c == "E":
	  		x += 1
	  	if c == "W":
	  		x -= 1

  fout.write(str(result) + "\n")
    