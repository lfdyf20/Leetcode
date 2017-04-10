class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = {0:-1}
        balance = maxlen = 0
        for i,num in enumerate(nums):
        	balance += num-0.5
        	maxlen = max( maxlen, i-index.setdefault(balance, i) )
        return maxlen



nums = [0,1,0]

sl = Solution()
print( sl.findMaxLength( nums ) )