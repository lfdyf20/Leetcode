class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        
        def calculate(i, j):
            if dp[i][j] or j==i+1:
                return dp[i][j]
            coins = 0
            for k in range(i+1, j):
                coins = max( coins, nums[i]*nums[k]*nums[j]+calculate(i,k)+calculate(k,j)  )
            dp[i][j] = coins
            return coins
            
        return calculate(0, n-1)


        # if not nums:
        # 	return 0
        # if len(nums) == 1:
        # 	return nums[0]
        # if len(nums) == 2:
        # 	return nums[0]*nums[1] + max(nums[0],nums[1])
        # res = 0
        # while len(nums)>3:
        # 	curr = min(nums[1:-1])
        # 	ind = nums.index( curr )
        # 	res += nums[ind-1]*curr*nums[ind+1]
        # 	nums.pop(ind)
        # res += nums[0]*nums[1]*nums[2] + nums[0]*nums[2] + max(nums[0],nums[2])
        # return res


nums = [3, 1, 5, 8]
nums = [9,76,64,21,97,60]

sl = Solution()
print( sl.maxCoins( nums ) )