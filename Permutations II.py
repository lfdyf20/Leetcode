class Solution(object):
	def permuteUnique(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		res = [[]]
		for i in nums:
			temp = []
			for path in res:
				print("path: ",path)
				for t in range(len(path)+1):
					temp += [path[:t] + [i] + path[t:]]
					print(temp)
					if t < len(path) and path[t]== i:
						print("here")
						break
			res = temp
		return res

	# def mySolution(self, nums):









nums = [1,2,1]

sl = Solution()
print( sl.permuteUnique( nums ) )


# print( [a + b for a in [1,2] for b in [3,4]] )
