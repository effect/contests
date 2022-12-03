# f = open("test.in")
f = open("a.in")

mapping = {
	"A": "Rock", 
	"B": "Paper", 
	"C": "Scissors", 
	"X": "Rock", 
	"Y": "Paper", 
	"Z": "Scissors", 
}

points = {
	"Rock": 1, 
	"Paper": 2, 
	"Scissors": 3, 
}

# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
defeat = {
	"Rock": "Scissors", 
	"Scissors": "Paper", 
	"Paper": "Rock", 
}

def points_for_shape(line):
	s = mapping[line[-1]]
	return points[s]

def outcome_for_first(line): 
	s1 = mapping[line[0]]
	s2 = mapping[line[-1]]
	if s1 == s2:
		return 3
	if defeat[s1] == s2:
		return 6
	return 0


lines = f.readlines()

result = 0
for line in lines:
	line = line.strip()
	result += points_for_shape(line)
	result += (6 - outcome_for_first(line))
print(result)
