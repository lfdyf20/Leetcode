# class Solution(object):
# 	def combinationSum3(self, k, n, start=1, res = []):
# 		return [[i]+c for i in range(start,10) 
# 				for c in self.combinationSum3(k-1,n-i,i+1)] if k > 1 else [[], [[n]]][start<=n<=9]



class Solution(object):
	def combinationSum3(self, k, n):
		"""
		:type k: int
		:type n: int
		:rtype: List[List[int]]
		"""
		return self.combination_sum_helper(k, n, 1)

	def combination_sum_helper(self, k, n, start):
		combination = []
		for i in range(start, 10):
			print( 'i1:', i )
			if i > n/k:  # prunning for candidate num greater than n/k
				print('i,n,k:',i,n,k  )
				return combination
			if k == 1:  # boundary condition: only one number left
				if i == n: 
					return [[i]]
				else:
					continue
			for c in self.combination_sum_helper(k-1, n-i, i+1):
				print( 'i2:', i )
				print('c:', c)
				print('combination:', combination)
				combination.append([i]+c)
				print('combination:', combination)
		return combination


k = 3
n = 9
sl = Solution()
res = sl.combinationSum3( k ,n )
print( res )



