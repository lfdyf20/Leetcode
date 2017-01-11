class Solution(object):
	def divide(self, dividend, divisor):
		"""
		:type dividend: int
		:type divisor: int
		:rtype: int
		"""
		positive = (dividend < 0) is (divisor < 0)
		dividend, divisor = abs(dividend), abs(divisor)
		res = 0
		while dividend >= divisor:
			temp, i = divisor, 1
			while dividend >= temp:
				dividend -= temp
				res += i
				i <<= 1
				temp <<= 1
		if not positive:
			res = -res
		return min(max(-2147483648, res), 2147483647)
		
		# neg = False
		# if dividend == 0:
		# 	return 0
		# if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
		# 	neg = True
		# dividend, divisor = abs(dividend), abs(divisor)
		# count = 0
		# while dividend >= divisor:
		# 	dividend -= divisor
		# 	count += 1
		# return count if not neg else 0-count


dividend, divisor = -20, 3

sl = Solution()
print( sl.divide( dividend, divisor ) )