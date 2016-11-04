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
			# print( 'i1:', i )
			if i > n/k:  # prunning for candidate num greater than n/k
				# print('i,n,k:',i,n,k  )
				return combination
			if k == 1:  # boundary condition: only one number left
				if i == n: 
					return [[i]]
				else:
					continue
			for c in self.combination_sum_helper(k-1, n-i, i+1):
				# print( 'i2:', i )
				# print('c:', c)
				# print('combination:', combination)
				combination.append([i]+c)
				# print('combination:', combination)
		return combination

	def cb3(self, k, n ):
		def travel( nums, k, n, path, res ):
			if n < 0:
				return
			if k == 0:
				if n != 0:
					return
				if n == 0:
					if path not in res:
						res.append( path )
					return
			if len(nums) < k:
				return
			if len(nums) == k:
				if sum(nums) == n:
					res.append( path+nums )
				return
			travel( nums[1:], k, n, path, res )
			travel( nums[1:], k-1, n-nums[0], path + [nums[0]], res )

		res = []
		nums = [i for i in range(1,10)]
		travel( nums, k, n, [], res )
		return res


	def cs3oneline( self, k, n ):
		from itertools import combinations

		return [c for c in combinations(range(1,10), k) if sum(c)==n]


k = 3
n = 15
sl = Solution()
print(sl.combinationSum3( k ,n ))
print(sl.cb3(k, n))
print(sl.cs3oneline(k, n))



