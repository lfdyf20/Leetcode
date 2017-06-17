from tryFunc import timer

class Solution(object):
	@timer
	def minCut(self, s):
		"""
		:type s: str
		:rtype: int
		""" 
		if not s:
			return 0

		if s == s[::-1]:
			return 0
		for i in range(1, len(s)):
			
			if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
				return 1
		count = [ [-1]*len(s) for _ in range(len(s))]

		def dp(i, j):
			# print(s[i:j])
			if count[i][j] != -1:
				return count[i][j]
			if j == i:
				count[i][j] = 0
				return count[i][j]
			if j == i + 1:
				if s[i] == s[j]:
					count[i][j] = 0
				else:
					count[i][j] = 1
				return count[i][j]
			if s[i:j+1] == s[i:j+1][::-1]:
				count[i][j] = 0
				return count[i][j]
			minCount = float('inf')
			for k in range(i, j):
				minCount = min(minCount, dp(i,k) + dp(k+1,j) + 1)
			count[i][j] = minCount
			return count[i][j]

		return dp(0, len(s)-1)

	def online(self, s):
		# acceleration
		if s == s[::-1]:
			return 0
		for i in range(1, len(s)):
			if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
				return 1

		# algo
		cut = [x for x in range(-1, len(s))]
		for i in range(len(s)):
			r1, r2 = 0, 0
			while i-r1 >= 0 and i+r1 < len(s) and s[i-r1]==s[i+r1]:
				cut[i+r1+1] = min(cut[i+r1+1], cut[i-r1]+1)
				r1 += 1
			while i-r2 >= 0 and i+r2+1 < len(s) and s[i-r2] == s[i+r2+1]:
				cut[i+r2+2] = min(cut[i+r2+2], cut[i-r2]+1)
				r2 += 1
		print(cut)
		return cut[-1]






s = "aabc"
# s = "apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"

sl = Solution()
# print( sl.minCut( s ) )
print( sl.online(s) )