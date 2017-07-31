class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, deepth, n = 0, 0, len(nums)
        visited = [False] * n
        for i in range(n):
        	while not visited[i]:
        		visited[i] = True
        		i, deepth = nums[i], deepth + 1
        	res = max(res, deepth)
        	deepth = 0
        return res


nums = [5,4,0,3,1,6,2]

sl = Solution()
print( sl.arrayNesting( nums ) )