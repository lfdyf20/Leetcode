class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(  len( nums )-1, 0, -1 ):
        	if nums[i] == nums[i-1]:
        		nums.pop(i)
        return len(nums)

# class Solution(object):
#     def removeDuplicates(self, nums):
#     	"""
#     	online: speed
#     	"""
#         i=1
#         j=1
#         a=len(nums)
#         while i<a:
#             if nums[i]>nums[i-1]:
#                 nums[j]=nums[i]
#                 j+=1
#             i+=1
#         return len(set(nums))

nums = [1,1,2]
sample = Solution()
print(sample.removeDuplicates( nums ))
print(nums)