class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """ 
        if len(s)<10:
        	return []
        dic = {}
        res = []
        for i in range(len(s)-9):
        	curr = s[i:i+10]
        	print(curr)
        	if curr in dic:
        		if dic[curr] == 1:
        			res.append(curr)
        			dic[curr] += 1
        	else:
        		dic[curr] = 1
        return res


# s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
s = "AAAAAAAAAAAAA"

sl = Solution()
print( sl.findRepeatedDnaSequences( s ) )