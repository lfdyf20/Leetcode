class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for i in nums:
        	if i in dic:
        		dic[i] += 1
        	else:
        		dic[i] = 1
        sortedDic = sorted( dic, key = lambda x:dic[x] )
        return (sortedDic[::-1])[0:k]




k = 2
nums = [1,1,1,1,2,2,2,3,3,4]
sample = Solution()
print( sample.topKFrequent( nums, k) )