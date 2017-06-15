import numpy as np
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [ [False]*(len(s)+1) for _ in range(len(p)+1) ]
        dp[0][0] = True

        if s == "" and p == "*":
        	return True

        for i in range(1, len(p)+1):
        	for j in range(1, len(s)+1):
        		if p[i-1] == '*':
        			for k in range(0, len(s)+1):
        				if dp[i-1][k] == True:
        					for t in range(k, len(s)+1):
        						dp[i][t] = True
        					break
        			break
        		if p[i-1] == '?':
        			dp[i][j] = dp[i-1][j-1]
        			continue
        		dp[i][j] = dp[i-1][j-1] and p[i-1]==s[j-1]
        # print(np.array(dp))
        return dp[-1][-1]


    def online(self, s, p):
    	si, pi, starInd, match = 0, 0, -1, 0
    	while si < len(s):
    		if pi<len(p) and (p[pi]=='?' or p[pi]==s[si]):
    			pi += 1
    			si += 1
    		elif pi<len(p) and p[pi]=='*':
    			starInd = pi
    			match = si
    			pi += 1
    		elif starInd!=-1:
    			pi = starInd + 1
    			match += 1
    			si = match
    		else:
    			return False
    	while pi < len(p) and p[pi] == '*':
    		pi += 1
    	return pi == len(p) 



s = "abefcdgiescdfimde"
p = "ab*cd?i*de"

s = "abbc"
p =  "?bbc"

s = "aa"
p = "a"

s = "a"
p = "a*"

s = "aa"
p = "a*"

s = "ab"
p = "?*"

s = "aab"
p = "c*a*b"

s = ""
p = "*"

s = "aa"
p = "*"

s = "aaaa"
p = "***a"

sl = Solution()
print( sl.isMatch( s, p ) )
print( sl.online( s, p) )


