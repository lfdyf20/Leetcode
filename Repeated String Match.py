class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        maxRep = len(B) // len(A) + 2
        AR = ""
        for i in range(1, maxRep+1):
        	AR += A
        	if B in AR:
        		return i
        else:
        	return -1



A, B = "abcd", "cdabcdab"

sl = Solution()
print( sl.repeatedStringMatch( A, B ) )