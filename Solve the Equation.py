import re

class Solution(object):
	def solveEquation(self, equation):
		"""
		:type equation: str
		:rtype: str
		"""
		equation = re.sub(r'\+', ' +', equation)
		equation = re.sub(r'\-', ' -', equation)
		# print(equation)
		left, right = equation.split('=')
		left, right = left.split(), right.split()
		# print(left, right)
		
		def process(exp):
			cx, cs = 0, 0
			for part in exp:
				if part[-1] == 'x':
					try:
						cx += int(part[:-1])
					except:
						cx += int(part[:-1] + '1')
				else:
					cs += int(part)
			return cx, cs

		lx, ls = process(left)
		rx, rs = process(right)
		# print(lx, rx, ls, rs)
		if lx == rx:
			if ls != rs:
				return "No solution"
			else:
				return "Infinite solutions"
		else:
			return "x={}".format( int((rs-ls)/(lx-rx)) )


	def online(self, equation):
		left, right = equation.split('=')
		print(left, right)
		left = re.findall(r'(\d)x')











equation = "x+5-3+x=6+x-2"
# equation = "x=x"
# equation = "2x=x"
# equation = "x=x+2"

sl = Solution()
print( sl.solveEquation( equation ) )
print( sl.online(equation) )