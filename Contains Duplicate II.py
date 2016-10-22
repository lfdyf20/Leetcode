class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        rec = {}
        for ind, i in enumerate(nums):
            if i in rec:
                if ind - rec[i] <= k:
                    return True
                else:
                    rec[i] = ind
                    continue
            else:
                rec[i] = ind
        return False
        # if len(nums)<=k:
        #     return len(nums) >  len(set(nums))

        # hashSet=set(nums[:k])
        # if len(hashSet) < k:
        #     return True

        # for i in xrange(k,len(nums)):
        #     hashSet.add(nums[i])
        #     if len(hashSet)==k:
        #         return True
        #     else:
        #         hashSet.remove(nums[i-k])
        # return False
        


sample = Solution()
nums = [1,2]
k = 1
print(sample.containsNearbyDuplicate(nums, k))

