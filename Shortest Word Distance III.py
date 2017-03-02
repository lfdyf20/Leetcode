class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dic = {}
        for i, word in enumerate(words):
        	if word in dic:
        		dic[ word ].append( i )
        	else:
        		dic[ word ] = [i]

        return min( abs(x-y) for x in dic[word1] for y in dic[word2] if x!=y )



words = ["practice", "makes", "perfect", "coding", "makes"]
word1, word2 = "makes", "makes"

sl = Solution()
print( sl.shortestWordDistance( words, word1, word2 ) )