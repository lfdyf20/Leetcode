class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        res = []
        self.travel(word, 0, "", 0, res)
        return res


    def travel(self, word, pos, curr, count, res):
    	if pos == len(word):
    		res.append( curr+str(count) if count>0 else curr )
    	else:
    		self.travel( word, pos+1, curr, count+1, res )
    		self.travel( word, pos+1, curr + (str(count) if count>0 else '') + word[pos], 0, res )


    	


word = "word"

sl = Solution()
print( sl.generateAbbreviations( word ) )