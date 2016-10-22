class Solution(object):
	def wordPattern(self, pattern, str):
		"""
		:type pattern: str
		:type str: str
		:rtype: bool
		"""
		s = pattern
		t = str.split()
		return map(s.find, s) == map(t.index, t)
		
		# rec = {}
		# pl = list( pattern )
		# sl = str.split()

		# if len(sl) != len(pl) or len(set(sl)) != len(set(pl)):
		# 	return False

		# for i,j in zip(pl, sl):
		# 	if i not in rec:
		# 		rec[i] = j
		# 	else:
		# 		if rec[i] != j:
		# 			return False
		# rec = {}
		# for i,j in zip(sl, pl):
		# 	if i not in rec:
		# 		rec[i] = j
		# 	else:
		# 		if rec[i] != j:
		# 			return False
		# return True

		




pattern, str = "abaa", "dog cat cat dog"

sl = Solution()
print( sl.wordPattern( pattern, str ) )