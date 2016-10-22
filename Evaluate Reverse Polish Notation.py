class Solution(object):
	def evalRPN(self, tokens):
		"""
		:type tokens: List[str]
		:rtype: int
		"""
		stack = []
		for t in tokens:
			if t not in ["+", "-", "*", "/"]:
				stack.append(int(t))
			else:
				r, l = stack.pop(), stack.pop()
				if t == "+":
					stack.append(l+r)
				elif t == "-":
					stack.append(l-r)
				elif t == "*":
					stack.append(l*r)
				else:
					if l*r < 0 and l % r != 0:
						stack.append(l//r+1)
					else:
						stack.append(l//r)
		return stack.pop()
	#  time limit exceeded
	# 	stack = []
	# 	operator = ["+", "-", "*", "/"]
	# 	for i in tokens:
	# 		if i not in operator:
	# 			stack.append(int(i))
	# 		else:
	# 			b = stack.pop()
	# 			a = stack.pop()
	# 			stack.append( self.compute(a, b, i) )
	# 		print(stack)
	# 	return stack[-1]


	# def compute( self, a, b, op ):
	# 	if op == "+":
	# 		return a+b
	# 	elif op == "-":
	# 		return a-b
	# 	elif op == "*":
	# 		return a*b
	# 	elif op == "/":
	# 		if a*b < 0 and a%b != 0:
	# 			return a//b+1
	# 		else:
	# 			return a//b
	# 	else:
	# 		return        



tokens = ["2", "1", "+", "3", "*"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# tokens = ["4","-2","/","2","-3","-","-"]

sl = Solution()
print( sl.evalRPN( tokens ) )
