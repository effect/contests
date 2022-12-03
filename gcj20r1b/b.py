import sys

fin = sys.stdin
fout = sys.stdout
ferr = sys.stderr

nt, a, b = (int(x) for x in fin.readline().split())
r = a

def search(d):
    for x in range(-d - 1, d + 1):
        for y in range(-d - 1, d + 1):
            fout.write(" ".join([str(x), str(y)]))
            fout.write('\n')
            fout.flush()

            res = fin.readline().strip()
            if res == "CENTER":
                return


for tn in range(nt):
    w = 10 ** 9
    d = w - r
    search(d)
    
