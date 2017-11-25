class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for x in ops:
        	if x == "+":
        		stack.append( stack[-1] + stack[-2] )
        	elif x == "D":
        		stack.append( stack[-1]*2 )
        	elif x == "C":
        		stack.pop()
        	else:
        		stack.append( int(x) )
        return sum(stack)
        



ops = ["5","-2","4","C","D","9","+","+"]
ops = []

sl = Solution()
print( sl.calPoints( ops ) )