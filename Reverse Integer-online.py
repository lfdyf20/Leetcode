class Solution(object):
	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		MAX, MIN = 2147483647, -2147483648
		isNeg = 1 if str(x)[0] == '-' else 0
		res = 0

		nlist = [i for i in str(x)]
		nlist.reverse()
		if isNeg:
			nlist.pop()
			nlist.insert(0, '-')
		k = ''
		for n in nlist:
			k += n
		res = int(k)

		if res > MAX or res < MIN - 1:
			return 0

		return res

x = int(raw_input("Please enter an integer: "))
solution = Solution()
x = 100
print solution.reverse(x)
