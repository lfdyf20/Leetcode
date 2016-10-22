class Solution(object):
	def removeKdigits(self, num, k):
		"""
		:type num: str
		:type k: int
		:rtype: str
		"""

		while k > 0:
			i = 0
			while i < len( num ) - 1:
				if num[i]>num[i+1]:
					break
				i += 1
			num = num[:i] + num[i+1:]
			k = k - 1

		if len(num) == 0:
			return "0"
		else:
			return str( int(num) )
			



num = "10432219"
k =  3

sl = Solution()
print( sl.removeKdigits( num, k ) )