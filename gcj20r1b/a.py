import sys

fin = sys.stdin
fout = sys.stdout

nt = int(fin.readline())

def get_symbol(is_x, dir):
	if is_x:
		if dir > 0:
			return "E"
		else:
			return "W"
	else:
		if dir > 0:
			return "N"
		else:
			return "S"

def solve(x, y, bit, mx, my):
	# print("x", x, "y", y, "bit", bit, "mx", mx, "my", my, sep=" ")
	if x < 0:
		yield from solve(-x, y, bit, -mx, my)
	elif y < 0:
		yield from solve(x, -y, bit, mx, -my)
	elif bit > 0:
		if x > y:
			yield get_symbol(True, mx)
			yield from solve(x - bit, y, bit >> 1, mx, my)
		else:
			yield get_symbol(False, my)
			yield from solve(x, y - bit, bit >> 1, mx, my)

def output(s):
	fout.write(s)
	fout.write('\n')

for tn in range(nt):
  fout.write("Case #" + str(tn + 1) + ": ")

  x, y = (int(a) for a in fin.readline().split())
  if (abs(x) + abs(y)) % 2 != 1:
  	output("IMPOSSIBLE")
  	continue

  bit = 1
  while (bit - 1) < (abs(x) + abs(y)):
  	bit <<= 1
  bit >>= 1

  res = "".join(solve(x, y, bit, 1, 1))
  output(res[::-1])
    