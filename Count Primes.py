class Solution(object):
	def countPrimes(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n < 3:
			return 0
		primes = [True] * n
		primes[0] = primes[1] = False
		for i in range(2, int(n ** 0.5) + 1):
			if primes[i]:
				primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
		print(primes)
		return sum(primes)

		# if n == 0:
		# 	return 0
		# if n<=3:
		# 	return n-2
		# count = 2
		# prime = [2,3]
		# for i in range(4, n):
		# 	print(prime)
		# 	isPrime = True
		# 	for j in prime:
		# 		if i % j == 0:
		# 			isPrime = False
		# 			break
		# 	if isPrime:
		# 		prime.append(i)
		# 		count += 1 
		# print(prime)
		# return count

		


solution = Solution()
n = 10
print(solution.countPrimes(n))