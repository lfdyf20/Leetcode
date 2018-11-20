class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        rec = {"U":0, "L":0}
        for move in moves:
        	if move in "UD":
        		rec[ "U" ] += [-1, 1][move=="U"]
        	if move in "LR":
        		rec[ "L" ] += [-1, 1][move=="L"]
        return all( map(lambda x:x==0, rec.values() ))
        



moves = "LDRRLRUULR"

sl = Solution()
print( sl.judgeCircle( moves ) )