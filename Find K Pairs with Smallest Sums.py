import itertools
import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """ 
        
        return sorted(itertools.product(nums1, nums2), key=sum)[:k]

    def other(self, nums1, nums2, k):
    	queue = []

    	def push(i, j):
    		if i < len(nums1) and j < len(nums2):
    			heapq.heappush(queue, (nums1[i] + nums2[j], i,j) )

    	push(0, 0)
    	res = []
    	while  len(res) < k and queue:
    		_, i, j = heapq.heappop( queue )
    		res.append( [i,j] )
    		push(i, j+1)
    		if j == 0:
    			push(i+1, 0)
    	return res





       	

          



nums1 =[1,1,2]
nums2 =[1,2,3]
k = 10

sl = Solution()
print( sl.kSmallestPairs( nums1, nums2, k ) )
print( sl.other(nums1, nums2, k) )


print([1,2][False])