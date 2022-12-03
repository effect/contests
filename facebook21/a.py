FIRST_PART = True
N = 26
INF = 1000000

def index(letter):
	return ord(letter) - ord("A")

def get_dist(is_first_part, fin):
	dist = [[INF] * N for i in range(N)]
	if is_first_part:
		VOWELS = ["A", "E", "I", "O", "U"]
		VOWEL_INDECIES = [index(letter) for letter in VOWELS]

		for ca in range(N):
			for cb in range(N):
				if ca == cb:
					dist[ca][cb] = 0
					continue

				is_ca_vowel = ca in VOWEL_INDECIES
				is_cb_vowel = cb in VOWEL_INDECIES
				if is_ca_vowel != is_cb_vowel:
					dist[ca][cb] = 1
				else:
					dist[ca][cb] = 2
	else:
		k = int(fin.readline())
		for i in range(k):
			ab = fin.readline()
			dist[ index(ab[0]) ][ index(ab[1]) ] = 1
		for i in range(N):
			dist[i][i] = 0

		for k in range(N):
			for i in range(N):
				for j in range(N):
					dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

	return dist


with open("a.in") as fin, open("a.out", "w") as fout:
	T = int(fin.readline())
	for t in range(T):
		fout.write("Case #" + str(t + 1) + ": ")

		s = fin.readline().strip()
		print(s)
		dist = get_dist(FIRST_PART, fin)

		res = INF
		for i in range(N):
			cur = 0
			for c in s:
				cur += dist[index(c)][i]
			res = min(res, cur)
			print(chr(ord("A") + i) + ": " + str(cur))

		if res < INF:
			fout.write(str(res))
		else:
			fout.write("-1")
		fout.write("\n")

		# print()
		# for a in dist:
		# 	print(a)