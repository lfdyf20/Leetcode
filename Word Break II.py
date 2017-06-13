import numpy as np
class Solution(object):
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: List[str]
		""" 
		return self.dp(s, wordDict, {})

	def dp(self, s, wordDict, memo):
		if s in memo:
			return memo[s]
		if not s:
			return []

		res = []
		for word in wordDict:
			if s.startswith(word):
				if len(word) == len(s):
					res.append(word)
				else:
					resultOfRest = self.dp( s[len(word):], wordDict, memo )
					for item in resultOfRest:
						item = word + ' ' + item
						res.append(item)
		memo[s] = res
		return res
			



s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
sl = Solution()
print( sl.wordBreak( s, wordDict ) )