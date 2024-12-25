f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

def get_register(index):
	return int(lines[index].split()[-1])

A, B, C = (get_register(i) for i in range(3))
p = [int(x) for x in lines[-1].split()[-1].split(',')]

def combo(operand):
	if operand <= 3: 
		return operand
	if operand == 4:
		return A
	if operand == 5:
		return B
	if operand == 6:
		return C
	print("WTF")
	return "WTF"

def division(instruction, operand):
	global A, B, C
	denom = 2 ** combo(operand)
	result = A // denom
	if instruction == 0:
		A = result
	if instruction == 6:
		B = result
	if instruction == 7:
		C = result


result = []
pointer = 0
while pointer < len(p):
	instruction, operand = p[pointer], p[pointer + 1]
	if instruction in [0, 6, 7]:
		division(instruction, operand)
	if instruction == 1:
		B ^= operand
	if instruction == 2:
		B = combo(operand) % 8
	if instruction == 3:
		if A:
			pointer = operand - 2
	if instruction == 4:
		B ^= C
	if instruction == 5:
		result.append(str(combo(operand) % 8))
	pointer += 2

print(",".join(result))