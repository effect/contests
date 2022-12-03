import sys

fin = sys.stdin
fout = sys.stdout

nt = int(fin.readline())


for tn in range(nt):
    fout.write("Case #" + str(tn + 1) + ": ")
    s = fin.readline().strip()

    s = "0" + s + "0"
    s = list(s)
    bal = 0
    pos = 1
    prev_value = 0
    while pos < len(s):
    	cur_value = int(s[pos])
    	# print(pos, cur_value)
    	diff = cur_value - prev_value
    	if diff > 0:
    		s.insert(pos, "(" * diff)
    		pos += 1
    	if diff < 0:
    		diff *= -1
    		s.insert(pos, ")" * diff)
    		pos += 1
    	pos += 1
    	prev_value = cur_value
    	# print(s)

    fout.write("".join(s[1:-1]))
    fout.write('\n')
    