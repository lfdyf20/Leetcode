import math
class Solution(object):
	def trailingZeroes(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		#print len( str(math.factorial(n)).rstrip("0") )
		return len( str(math.factorial(n)) ) - len( str(math.factorial(n)).rstrip("0")) 
			
	def mySolution(self, n):
		
		if n < 5:
			return 0
		i = 5
		res = 0
		while i <= n:
			res = res + n/i
			i = i * 5
		return res


	def Online(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		# if  n >= 5:
		# 	return self.trailingZeroes(n/5) + n/5
		# else:
		# 	return 0

		return 0 if n<5 else n//5 + self.trailingZeroes(n//5)





n = 3125
#print math.factorial(n)
print(n/5 + n/25 + n/125 + n/625 + n/3125 + n/(3125*5) + n/(3125*25))
sample = Solution()
print("trailingZeroes:",sample.trailingZeroes(n))
print("mySolution:",sample.mySolution(n))