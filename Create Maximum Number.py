class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def prep(nums, k):
        	"""
        	@1
        	"""
        	drop = len(nums) - k
        	greater = []
        	for num in nums:
        		while drop and greater and greater[-1] < num:
        			greater.pop()
        			drop -= 1
        		greater.append(num)
        	return greater[:k]

        def merge(a, b):
        	return [max(a, b).pop(0) for _ in a+b]

        return max(merge(prep(nums1, i), prep(nums2, k-i))
        			for i in range(k+1) 
        			if i <= len(nums1) and k-i <= len(nums2))



nums1, nums2, k = [3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5

sl = Solution()
print( sl.maxNumber( nums1, nums2, k ) )



"""
@1
I thought of the same approach, which is applied to another problem.
For an in[] array, and int K, form maximum number, while maintaining order.
Example - [2,3,9,8,2,6], and K = 3, the maximum number formed is [9,8,6].
[2] - Add, while remaining K = 2, Remaining elements is 5
[2,3] - Add 3, while remaining K = 1, Remaining elements is 4
[9] - Pop 3 and 2, since 9 is greater than both and remaining K = 2 < elements = 3
[9,8] - Add 8, less than 9, and remainging K = 1 < elements = 2
[9,8,2] - Add 2, less than 8, and remainging K = 0 < elements = 1
[9,8,6] - Pop 2, Add 6, since popping 2 makes K = 1, and element left is 1, which is 6
"""