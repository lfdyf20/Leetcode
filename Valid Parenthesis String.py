class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # From left to right
        p = a = 0

        for i in s:
        	if i == "(":
        		p += 1
        	elif i == ")":
        		if p <= 0 and a <= 0:
        			return False
        		if p > 0:
        			p -= 1
        		else:
        			a -= 1
        	else:
        		a += 1

        # from right to left
        pp = aa = 0

        for i in s[::-1]:
        	if i == ")":
        		pp += 1
        	elif i == "(":
        		if pp <= 0 and aa <= 0:
        			return False
        		if pp > 0:
        			pp -= 1
        		else:
        			aa -= 1
        	else:
        		aa += 1

        return aa >= pp and a >= p




s = "()*((*()**)"
s = "()"
s = "(*)"
s = "(*))"
s = "(((**"
s = "(())((())()()(*)(*()(())())())()()((()())((()))(*"

sl = Solution()
print( sl.checkValidString( s ) )