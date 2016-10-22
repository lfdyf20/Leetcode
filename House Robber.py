class Solution(object):
	def rob(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		
		# if nums == []:
		# 	return 0
		# if len( nums ) == 1:
		# 	return nums[0]
		# return max( nums[0] + self.rob(nums[2:]), nums[1] + self.rob(nums[3:])) 
		m_low = m_high = 0

		for n in nums:
			m_high, m_low = max(m_low + n, m_high), m_high
		return m_high
		








nums = [114,117,207,117,235,82,90,67,143,146,53,108,200,91,80,223,58,170,110,236,81,90,222,160,165,195,187,199,114,235,197,187,69,129,64,214,228,78,188,67,205,94,205,169,241,202,144,240]
sample = Solution()
print sample.rob(nums)
