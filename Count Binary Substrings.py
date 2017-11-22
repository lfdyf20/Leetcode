class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
        	return 0
        curr, currCount = s[0], 1
        pre, preCount = None, 0
        res = 0
        for ss in s[1:]:
        	if ss == curr:
        		currCount += 1
        		if currCount <= preCount:
        			res += 1
        	else:
        		pre, preCount = curr, currCount
        		curr, currCount = ss, 1
        		res += 1
        return res	
        		

    def online(self, s):
    	count = [1]
    	for pre, curr in zip(s, s[1:]):
    		if curr == pre:
    			count[-1] += 1
    		else:
    			count.append(1)
    	res = 0
    	for pre, curr in zip(count, count[1:]):
    		res += min(pre, curr)
    	return res




s = "00110011"
s = "10101"
s = "001110011"

sl = Solution()
print( sl.countBinarySubstrings( s ) )
print( sl.online(s) )