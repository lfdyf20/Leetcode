import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        sortList = []
        for i in matrix:
        	for j in i:
        		sortList.append( j )
        sortList.sort()
        return sortList[k-1]
        
    def ks(self, matrix, k):
        return list(heapq.merge(*matrix))[k-1]




matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
sl = Solution()
print( sl.kthSmallest(matrix, k) )
print( sl.ks(matrix, k) )
