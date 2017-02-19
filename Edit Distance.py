class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n, m = len(word1), len(word2)
        res = [ [0]*(m+1) for _ in range(n+1) ]
        for i in range(1,n+1):
        	res[i][0] = i
        for i in range(1,m+1):
        	res[0][i] = i
        for i in range(1,n+1):
        	for j in range(1,m+1):
        		if word1[i-1] == word2[j-1]:
        			res[i][j] = res[i-1][j-1]
        		else:
        			res[i][j] = min( res[i-1][j-1]+1, res[i-1][j]+1, res[i][j-1]+1 )
        return res[-1][-1]



word1, word2 = "ajsdkad", "bjskado"
word1, word2 = "b", ""
sl = Solution()
print( sl.minDistance( word1, word2 ) )






## note
# http://web.stanford.edu/class/cs124/lec/med.pdf
# https://discuss.leetcode.com/topic/17639/20ms-detailed-explained-c-solutions-o-n-space/3