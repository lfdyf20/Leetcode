class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum([1 for i in S if i in J])



J, S = "aA", "aAAbbbb"

sl = Solution()
print( sl.numJewelsInStones( J, S ) )