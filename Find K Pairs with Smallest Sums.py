import itertools
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """ 
        
        return sorted(itertools.product(nums1, nums2), key=sum)[:k]
       	

          



nums1 =[1,1,2]
nums2 =[1,2,3]
k = 10

sl = Solution()
print( sl.kSmallestPairs( nums1, nums2, k ) )


print([1,2][False])