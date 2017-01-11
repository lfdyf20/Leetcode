import random
class ApoWorld(object):
	"""docstring for ApoWorld"""
	def __init__(self, amount):
		self.n = amount
		self.children = ""
		self.boy = self.girl = 0
		self.gen = [0, 1]

	def familyChildren(self):
		while random.choice(self.gen) == 1:
			self.boy += 1
			self.children += "B"
		self.girl += 1
		self.children += "G"

	def census(self):
		return self.children, self.boy/self.girl

	def haveSex(self):
		for i in range(self.n):
			self.familyChildren()
			self.children += "/"


world = ApoWorld( 10000 )
world.haveSex()
children, rate = world.census()
print(children)
print(rate)

		