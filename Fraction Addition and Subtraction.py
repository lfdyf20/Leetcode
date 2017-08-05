import re
import math
class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        ints = map(int, re.findall('[+-]?\d+', expression))
        A, B = 0, 1
        for a in ints:
        	b = next(ints)
        	A = A * b + a * B
        	B *= b
        	g = math.gcd(A, B)
        	A //= g
        	B //=g
        return "{}/{}".format(A, B)


expression = "-1/2+1/2+1/3"

sl = Solution()
print( sl.fractionAddition( expression ) )