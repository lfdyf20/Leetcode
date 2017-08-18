class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        stack = []
        for i in S.upper():
        	if i == '-': continue
        	stack.append(i)
        count = 0
        res = ''
        while stack:
        	res = stack.pop() + res
        	count += 1
        	if count % K == 0:
        		res = '-' + res
        return res[1:] if res and res[0] == '-' else res



S = "2-4A0r7-4k"
S = '---'
K = 3

sl = Solution()
print( sl.licenseKeyFormatting( S, K ) )