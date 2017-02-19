class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # res = []
        # dic = {"+":"-", "-":"+"}
        # for i in range( len(s)-1 ):
        #     if s[i] == s[i+1]:
        #         res.append( s[:i] + dic[s[i]]*2 + s[i+2:] )
        # return res

        return [s[:i]+"--"+s[i+2:] for i in range(len(s)-1) if s[i:i+2]=="++"]



s = "--"

sl = Solution()
print( sl.generatePossibleNextMoves( s ) )