class Solution(object):
	def diffWaysToCompute(self, input):
		"""
		:type input: str
		:rtype: List[int]
		""" 
		# return [a+b if c=="+" else a-b if c=='-' else a*b
		# 		for i, c in enumerate(input) if c in "+-*"
		# 		for a in self.diffWaysToCompute(input[:i])
		# 		for b in self.diffWaysToCompute(input[i+1:])] or [int[input]]
		# 		def diffWaysToCompute(self, input):
		return [a+b if c == '+' else a-b if c == '-' else a*b
				for i, c in enumerate(input) if c in '+-*'
				for a in self.diffWaysToCompute(input[:i])
				for b in self.diffWaysToCompute(input[i+1:])] or [int(input)]

	def dwtc(self, input):
		def helper(m, n, op):
			if op == "+":
				return m+n
			elif op == "-":
				return m-n
			else:
				return m*n

		if input.isdigit():
			return [int(input)]
		res = []
		for i in range(len(input)):
			if input[i] in "-+*":
				res1 = self.diffWaysToCompute(input[:i])
				res2 = self.diffWaysToCompute(input[i+1:])
				for j in res1:
					for k in res2:
						res.append(helper(j, k, input[i]))
		return res
		
	




input = "2*3-11*8+2-1"
sl = Solution()
print( sl.diffWaysToCompute(input) )
print( sl.dwtc(input) )