class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """ 
        ind = sorted(range(len(nums)), key = lambda x: nums[x])
        print(ind)
        for i in range(len(nums)-1):
            j = i + 1
            while j < len(nums) and nums[ind[j]] - nums[ind[i]] <= t:
                if abs(ind[i]-ind[j]) <= k:
                    return True
                j += 1
        return False
        # for i in range( len(nums)-k ):
        # 	# print( nums[i:1+i+k] )
        # 	a = nums[i+1: i+1+k]
        # 	b = min (  abs(max(a) - nums[i]), abs(min(a) - nums[i]))
        # 	if b <= t:
        # 		return True
        # return False



nums = [0,10,20,5,100]
k = 3
t = 5

sl = Solution()
print( sl.containsNearbyAlmostDuplicate( nums, k, t ) )