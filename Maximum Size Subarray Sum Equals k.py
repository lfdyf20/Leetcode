from collections import defaultdict
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res, sumVal = 0, 0
        dic = {0:-1}
        for i in range( len(nums) ):
        	sumVal += nums[i]
        	if sumVal not in dic:
        		dic[ sumVal ] = i
        	if sumVal - k in dic:
        		res = max( res, i - dic[ sumVal-k ] )
        return res






    def maxLengthElement(self, nums, k):
        dic = {}
        for num in nums:
        	newDic = {}
        	if num not in dic:
        		newDic[num] = 1
        	for ele in dic:
        		if ele+num in dic:
        			newDic[ ele+num ] = max( dic[ele+num], dic[ele]+1 )
        		else:
        			newDic[ ele+num ] = dic[ ele ] + 1
        	dic.update( newDic )
        return dic[ k ]



nums, k = [-2, -1, 2, 1], 1

sl = Solution()
print( sl.maxSubArrayLen( nums, k ) )