list = []
char = []
dict = {}
for i in range(1, 20):
	for j in range(1, 20):
		rs = i*j
		eq = '{0}x{1}={2}'.format(i, j, rs)
		eq1 = '{0}x{1}'.format(i, j)
		if rs in list:
			print('***', end=' ')
		else:
			if rs > 100:
				print(rs,'', end='')
			elif rs > 10:
				print('%s ' %rs, end='')
			elif rs:
				print('%s  ' %rs, end='')
		list.append(rs)
	print(' ')

print(len(dict))
print(sorted(dict))