import time
def reocrdTime( function ):
	def wrapper(*args, **kwargs):
		t1 = time.time()
		print( function(*args, **kwargs) )
		print( "function runtime is: ", time.time() - t1 )
	return wrapper

class Solution(object):
    @reocrdTime
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack = []
        low = float('-inf')
        for p in preorder:
        	if p < low:
        		return False
        	while stack and p > stack[-1]:
        		low = stack.pop()
        	stack.append( p )
        return True  

preorder = [5,3,2,1,4,10,7]

sl = Solution()
sl.verifyPreorder( preorder )


