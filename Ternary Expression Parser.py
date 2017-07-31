class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        stack = []
        for i in reversed(expression):
        	stack.append(i)
        	if stack[-2:-1] == ["?"]:
        		stack[-5:] = stack[ -3 if stack[-1] == 'T' else -5 ]
        return stack[0] 



expression = "T?T?F:5:3"

sl = Solution()
print( sl.parseTernary( expression ) )