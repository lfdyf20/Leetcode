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


    def bucket(self, nums, k, t):
        if t < 0:
            return False
        n = len(nums)
        dic = {}
        w = t + 1
        for i in range(n):
            m = nums[i] // w
            if m in dic:
                return True
            if m-1 in dic and abs(nums[i]-dic[m-1]) < w:
                return True
            if m+1 in dic and abs(nums[i]-dic[m+1]) < w:
                return True
            dic[m] = nums[i]
            if i >= k:
                del dic[nums[i-k]/w]
        return False





nums = [0,10,20,5,100]
k = 3
t = 5

sl = Solution()
print( sl.containsNearbyAlmostDuplicate( nums, k, t ) )