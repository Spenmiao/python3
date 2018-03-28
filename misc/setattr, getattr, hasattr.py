class Test:
	def __init__(self, name, age):
		self.name = name
		self.age = age

test = Test('mary', '18')
setattr(test, 'gender', 'male')
print(getattr(test, 'gender'))
print(hasattr(test, 'name'))
print(dir(test))
