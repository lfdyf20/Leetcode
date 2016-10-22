class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """ 
        s1 = set(nums1)
        s2 = set(nums2)
        result = s1 & s2
        return list(result)


nums1 , nums2 = [1,2,3,4,2,1], [2,2]
sample = Solution()
print(sample.intersection(nums1,nums2))
