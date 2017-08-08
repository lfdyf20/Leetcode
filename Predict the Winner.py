class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def score(l, r, memo):
        	if l > r: return 0
        	if l == r: return nums[l]
        	if not (l, r) in memo:
        		lv = -score(l+1, r, memo) + nums[l]
        		rv = -score(l, r-1, memo) + nums[r]
        		memo[(l,r)] = max(lv, rv)
        	return memo[(l,r)]

        res = score(0, len(nums)-1, {})
        return res >= 0

        



nums = [1, 5, 233, 7]

sl = Solution()
print( sl.PredictTheWinner( nums ) )