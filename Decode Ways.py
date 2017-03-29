class Solution(object):
	def numDecodings(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if s == "": return 0
		dp = [0 for x in range(len(s)+1)]
		dp[0] = 1
		for i in range(1, len(s)+1):
			if s[i-1] != "0":
				dp[i] += dp[i-1]
			if i != 1 and s[i-2:i] < "27" and s[i-2:i] > "09":  #"01"ways = 0
				dp[i] += dp[i-2]
		return dp[len(s)]
		








		# def travel(s):
		# 	print(s)
		# 	if s == "":
		# 		return 0
		# 	if s[0] == "0":
		# 		return 0
		# 	if len(s) <= 1:
		# 		return len(s)
		# 	if int( s[:2] ) <= 26:
		# 		if len(s) == 2 and s[1] != "0":
		# 			return 2
		# 		if len(s) == 2 and s[1] == "0":
		# 			return 1
		# 		else:
		# 			return travel(s[1:]) + travel(s[2:])
		# 	else:
		# 		return travel(s[1:])
		
		# if s == "":
		# 	return 0
		# return travel(s)




s = "1010"

sl = Solution()
print( sl.numDecodings( s ) )