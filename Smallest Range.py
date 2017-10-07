import heapq
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        pq = [ (num[0], i, 0) for i, num in enumerate(nums) ]
        heapq.heapify(pq)

        res = -1e9, 1e9

        right = max(num[0] for num in nums)

        while pq:
        	left, i, j = heapq.heappop( pq )
        	if right - left < res[1] - res[0]:
        		res = left, right
        	if j + 1 >= len( nums[i] ):
        		return list(res)

        	nextI = nums[i][j+1]
        	right = max(right, nextI)
        	heapq.heappush(pq, (nextI, i, j+1) )


        



nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]

sl = Solution()
print( sl.smallestRange( nums ) )