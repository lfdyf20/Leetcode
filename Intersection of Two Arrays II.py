class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """ 
        result = []
        dic = {}
        for i in nums1:
        	if i in dic:
        		dic[i] += 1
        	else:
        		dic[i] = 1
        for i in nums2:
        	if i in dic and dic[i] != 0:
        		result.append( i )
        		dic[i] -= 1 
        	else:
        		pass
        return result






nums1 = [1,2,2,3,4,4]
nums2 = [2,2,1,4,5]
sample = Solution()
print( sample.intersect( nums1, nums2 ) )
