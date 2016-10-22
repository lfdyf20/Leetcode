class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """ 
        return sorted(nums)[-k]



nums = [1,3,5,7,8]
k = 3
sl =Solution()
print( sl.findKthLargest(nums, k) )