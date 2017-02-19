from collections import Counter, defaultdict, deque
from itertools import combinations

a = {1:2, 3:4}
b = {1:5, 4:2}

class one(object):
	"""docstring for one"""
	def hello(self):
		self.a = 1
		def w():
			self.a += 1
		w()
		print(self.a)


one = one()
print( one.hello() )

a = 0 if 1 else 4
print(a)

a = 1
a += 1 if 1 else 2
print(a)
		