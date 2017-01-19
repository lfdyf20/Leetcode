class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        dic = {}
        for i in nums:
        	if i in dic:
        		dic[i] += 1
        	else:
        		dic[i] = 1
        for i in dic.items():
        	if i[1] != 3:
        		return i[0]


    def mysolution(self, nums):
        
        return nums
        





nums = [1,5,1,1,2,3,2,2,3,5,5]
sample = Solution()
print( sample.singleNumber( nums ) )
print( sample.mysolution(nums) )
