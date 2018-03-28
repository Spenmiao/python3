#str
x = "tTThTbe sum of 1 T+ 2sum is ".lstrip('sTse')
#print(x.replace('sum', 'sd', 1))
#print(x.center(49, '*'))
# print(x.upper())
# print(x.lower())
# print(x.capitalize())
print(len(x))

#sets
a = set('123456')
b = set('456789')
# print(b)
# print(a)
# print(a - b)
# print(a & b)
# print(a | b)
# print(a ^ b)

#dict
# print(range(1, 23).index(3,1, 13))
# dict
dict = {'id': 1456,
'name':'diisd'}
print(dict.get('id'))
print([i for i in dict.keys()])
print([(j, i) for i,j in dict.items()])