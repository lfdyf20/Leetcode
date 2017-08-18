class Solution(object):

	# REVIEW: to solve
	def lastRemaining(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		# return [ 1, 2 * (1 + n // 2 - self.lastRemaining(n // 2))][n != 1];
		# nums = range(1, n+1)
		# while len(nums) > 1:
		# 	nums = nums[1::2][::-1]
		# return nums[0]
		left = True
		remaining = n
		step, head = 1, 1
		while remaining > 1:
			if left or remaining % 2 == 1:
				head = head + step
			remaining = remaining // 2
			step *= 2
			left = not left

		return head 

	def lr(self, n):
		l = [ i for i in range(1,n+1)]
		while len(l) != 1:
			l = l[1::2]
			if len(l) == 1:
				return l[0]
			l = l[::-1]
		return l[0]







n = 10000000

sl = Solution()
print( sl.lastRemaining( n ) )
print( sl.lr(n) )

