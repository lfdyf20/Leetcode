import numpy as np
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """ 
        a = np.array( A )
        b = np.array( B )
        c = np.dot( a, b )
        return c.tolist()



A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]
B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

sl = Solution()
print( sl.multiply( A, B ) )