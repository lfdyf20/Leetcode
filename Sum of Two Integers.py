class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """ 
        count = []
        if a*b > 0 :
        	for i in range( abs(a) ):
        		count.append('a')
        	for j in range( abs(b) ):
        		count.append('b')
        	if a>0:
        		return len(count)
        	else:
        		return -len(count)
        else:
        	if abs(a)>abs(b):
        		for i in range( abs(a) ):
        			count.append('a')
        		for j in range( abs(b) ):
        			count.pop()
        		if a>0:
        			return len(count)
        		else:
        			return -len(count)
        	else:
        		for i in range( abs(b) ):
        			count.append('b')
        		for j in range( abs(a) ):
        			count.pop()
        		if b>0:
        			return len(count)
        		else:
        			return len(count)









a = 33
b = -24

sl = Solution()
print( sl.getSum( a, b ) )