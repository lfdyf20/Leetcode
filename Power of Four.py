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



num = 16
sl = Solution()
print( sl.isPowerOfFour(num) )

a = [[1,1,9,9],[4,5,6,3],[3,2,1,4],[5,3,7,3]]

for i in [0,2]:
	for j in [0,2]:
		print(i,j)
		