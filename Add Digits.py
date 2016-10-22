class Solution(object):
	def addDigits(self, num):
		"""
		:type num: int
		:rtype: int
		"""
		# result = num
		# if result <= 10:
		# 	return result
		# while  result > 10 :
		# 	numlist = list( str(result) )
		# 	result = 0
		# 	for digit in numlist:
		# 		result = result + int(digit)
						
		# return result
		x = num % 9
		if not x and num:
			return 9
		else:
			return x




num = 38

sample = Solution()
print sample.addDigits( num )
numlist = list(str(num))
print numlist