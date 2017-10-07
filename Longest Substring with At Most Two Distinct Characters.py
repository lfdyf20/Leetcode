class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2 or len(set(s)) <= 2:
        	return len(s)
        first, second, fc, sc, temp = s[0], None, 1, 0, 1
        res = 1
        for c in s[1:]:
        	print("first:{}:{} - second:{}:{} - res:{}".format(first,fc,second,sc,res))
        	if second is None:
        		if c == first:
	        		fc += 1
	        	else:
	        		second, sc, temp = c, 1, 1
	        		res = max(res, fc + sc)
	        	continue
        	if c == second:
        		sc += 1
        		temp += 1
        	elif c == first:
        		first, second, fc, sc, temp = second, first, sc, fc + 1, 1
        	else:
        		res = max(res, fc + sc) 
        		first, second, fc, sc, temp = second, c, temp, 1, 1         	   		
        res = max(res, fc + sc)
        return res


s = "eceba" # 3
# s = "eeee" # 4
# s = "ebbbb" # 5
# s = "aaabc" # 4
# s = "ababacccccc" # 7

sl = Solution()
print( sl.lengthOfLongestSubstringTwoDistinct( s ) )