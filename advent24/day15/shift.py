a = [1, 2, 3, 4, 5, 6]
print(a)
ind = 1
save = a[ind]
for i in range(ind + 1, len(a)):
	save, a[i] = a[i], save

print(a)

a = [1, 2, 3, 4, 5, 6]
ind = 1
save = a[ind]
for i in range(ind + 1, len(a)):
	save_new = a[i]
	a[i] = save
	save = save_new
print(a)