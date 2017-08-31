class Solution(object):
	# TODO: redo this, cause I didn't solve it this time
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subs = {()}
        for num in nums:
        	subs |= { sub + (num,) for sub in subs
        				if not sub or sub[-1] <= num }
        return [ sub for sub in subs if len(sub) > 1 ]



nums = [4, 6, 7, 7]

sl = Solution()
print( sl.findSubsequences( nums ) )