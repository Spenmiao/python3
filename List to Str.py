# list to str
list = ('name', 'gender', 'age')
str = ' '.join(list)
print(str)

list2 = [('name', 'mary'), ('gender','male'), ('age', '13')]
for i in list2:
	print(' '.join(i), ' ' ,end='')
