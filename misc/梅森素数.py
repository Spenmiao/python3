

def monisen(num):
	l = [2, ]
	for ints in range(3, 200):
		count = 1
		for i in range(2, ints):
			if ints % i == 0:
				count += 1
				break
		if count == 1:
			l.append(ints)
	
	monisen = [(p, m) for m in l for p in l if m == 2**p -1]
	result = monisen[num-1][1]
	return int(result)
print(monisen(3))


