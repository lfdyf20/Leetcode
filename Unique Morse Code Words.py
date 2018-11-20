class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        mapList = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        return len( {"".join(mapList[ord(x)-ord('a')]  for x in word) 
        	for word in words} )





words = ["gin", "zen", "gig", "msg"]

sl = Solution()
print( sl.uniqueMorseRepresentations( words ) )