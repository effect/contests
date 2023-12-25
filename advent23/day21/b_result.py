f = open("test.in")
# f = open("input.txt")

a1 = 3770  # size(wave(65))
a0 = 3885  # size(wave(64))
b = (34700 - 4 * a0 - a1) // 2  # 34700 == size(wave(65 + 131))
print(b)

def f(k):
	return k * k * a1 + (k + 1) * (k + 1) * a0 + ((2 * k + 1) * (2 * k + 1) - k * k - (k + 1) * (k + 1)) // 2 * b

for i in range(5):
	print(f(i))

k = 26501365 // 131
print(f(k))