class Solution(object):
	def longestValidParentheses(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		# s = ")" + s  
		stack, ans = [], 0
		for index in range(len(s)):
			element = s[index]
			if element == ")" and stack and stack[-1][1] == "(":
				stack.pop()
				ans = max(ans, index - stack[-1][0])
			else:
				stack.append((index, element))
		return ans

				




s = "(()(())"
s = "(())()(()"
s = ")()"
s = '())'
s = ")()())()()("
# s = "()()))))()()("
s = ")(((((()())()()))()(()))("

sl = Solution()
print( sl.longestValidParentheses( s ) )