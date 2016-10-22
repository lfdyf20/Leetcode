class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)<=k:
            return len(nums) >  len(set(nums))

        hashSet=set(nums[:k])
        if len(hashSet) < k:
            return True

        for i in xrange(k,len(nums)):
            hashSet.add(nums[i])
            if len(hashSet)==k:
                return True
            else:
                hashSet.remove(nums[i-k])
        return False
        """
        """
        d = {}
        t = 0
  		#for i in xrange(len(nums)):
		# 	t = nums[i]
		# 	if not t in d or i-d[t] > k:
		# 		d[t] = i
		# 	else:
		# 		return True
		# return False


# sample = Solution()
# nums = [1,2]
# k = 1
# print sample.containsNearbyDuplicate(nums, k)
nums = [1,1,3,4,5,1,3]
hashSet = set(nums)
print "hashSet:",hashSet
hashSet.add(6)
print "hashSet.add(6)=",hashSet

print 1 != 2
