class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return [dic[num], i]
            else:
                dic[target - num] = i
        # result = [0, 0]
        
        # for i in range( len(nums) ):
        	
        # 	#print i
        # 	result[0] = i
        # 	t = target - nums[i]
        # 	#print "i=",i, "first index=",result[0], "t=",t
        # 	if ( nums[i+1:].count( t )>0 ):
        		
        # 		result[1] = nums[i+1:].index( t )+i+1
        		
        # 		return  result




nums = [3,2,4]
target = 6



sample = Solution()
print(sample.twoSum(nums, target) )