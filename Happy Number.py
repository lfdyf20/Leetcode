class Solution(object):
	def isHappy(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		# record = [n]
		# while ( n!=1 ):
		# 	numList = list( str( n ) )
		# 	n = 0
		# 	for i in numList:
		# 		n = n + int(i)**2
		# 	if n in record:
		# 		return False
		# 	else:
		# 		record.append( n )
		# return True
		record = [n]
		res = n
		while res != 1:
			l = [ int(i) for i in str(res) ]
			res = 0
			for i in l:
				res += i**2
			if res in record:
				return False
			else:
				record.append( res )
		return True





n = 19
sample = Solution()
print(sample.isHappy( n ))
