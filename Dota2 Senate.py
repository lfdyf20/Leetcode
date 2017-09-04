from collections import Counter
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        res = {'R': 'Radiant', 'D':'Dire'}
        ban = Counter()
        while senate:
        	new = ""
	        for i in senate:
	        	if ban[ i ] > 0:
	        		ban[ i ] -= 1
	        	else:
	        		new += i
	        		ban[ chr(150-ord(i)) ] += 1
	        for c in 'RD':
	        	if new.count(c) > new.count(chr(150-ord(c))) * 2:
	        		return res[c]
	        senate = new
        



senate = "RDDRDDRDDR"
senate = "RDD"

sl = Solution()
print( sl.predictPartyVictory( senate ) )