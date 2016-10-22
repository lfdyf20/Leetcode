class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len( nums )
        # if n == 1:
        # 	return nums[0]
        # record = {}
        # for i in nums:
        # 	if record.has_key( i ):
        # 		record[i] = record[i] + 1
        # 		if record[i] > n/2.0:
        # 			return i
        # 	else:
        # 		record[i] = 1
        return sorted(nums)[len(nums)/2]
        