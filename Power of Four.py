class Solution(object):
	def isPowerOfFour(self, num):
		"""
		:type num: int
		:rtype: bool
		""" 
		if num == 0:
			return False
		while num%4 == 0:
			num = num/4
		if num == 1:
			return True
		else:
			return False

	def other(self, num):
		if num == 1: return True
		if num == 2: return False
		key = bin(num)[2:][::-1]
		if key.count('1') > 1:
			return False
		try:
			index = key.index('1')
		except:
			return False
		else:
			return index%2==0

	def isPowerOfFour(self, num):
		return num != 0 and num &(num-1) == 0 and num & 1431655765== num





num = 16
sl = Solution()
for num in [0,1,2,3,4,6,8,16,45, 64]:
	print( num, sl.isPowerOfFour(num) )
	print( num, sl.other(num) )

		