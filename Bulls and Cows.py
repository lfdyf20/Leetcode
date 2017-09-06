from collections import Counter
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        sc, gc = Counter(), Counter()
        A = B = 0
        for i, j in zip(secret, guess):
        	if i == j:
        		A += 1
        	else:
        		sc[i] += 1
        		gc[j] += 1
        B = sum( (sc & gc).values() )
        return "{}A{}B".format(A, B)


secret, guess = "1123", "0111"

sl = Solution()
print( sl.getHint( secret, guess ) )