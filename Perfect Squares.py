import math
import time
cache = {}
class Solution(object):
	def numSquares(self, n):
		"""
		:type n: int
		:rtype: int
		""" 
		global cache

		if n == 0:
			return 0
		if n < 0:
			return None
		if n in cache:
			return cache[n]
		else:
			answer = 1 + min( [self.numSquares(n-t*t) for t in range(1, int(math.sqrt(n))+1)] )
			cache[n] = answer
		return answer

	#     if n==0 or n==1:
	#     	return 1
	#     path = []
	#     res = []
	#     minLen = [float('inf')]
	#     start = time.time()
	#     self.findSl( n, path, minLen, res )
	#     print("runtime for func : ", time.time() - start)
	#     start = time.time()
	#     # minLen = len(min(res, key[-1]=len))
	#     print("runtime for search : ", time.time() - start)
	#     print(res)
	#     return minLen[-1]


	# def findSl( self, n, path, minLen, res ):
	# 	if len(path) >= minLen[-1] or len(path)>4:
	# 		return
	# 	if n==0:
	# 		res.append( path )
	# 		minLen.append( len(path) )
	# 	h = math.floor(math.sqrt(n))
	# 	while h:
	# 		self.findSl( n-h**2, path+[h**2],  minLen, res )
	# 		h -= 1

	# def ns(self, n):
	# 	h = int( n**0.5 )
	# 	cd = sorted([ i**2 for i in range(1, h) ], reverse=True)










n = 83
sl = Solution()
print( sl.numSquares(n) )
# print( sl.ns(n) )