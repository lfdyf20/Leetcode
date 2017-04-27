class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        p1, p2 = float('-inf'), float('-inf')
        minDis = float('inf')
        for i, word in enumerate(words):
        	if word == word1:
        		p1 = i
        		minDis = min(minDis, p1-p2)
        	if word == word2:
        		p2 = i
        		minDis = min(minDis, p2-p1)
        return minDis



words, word1, word2 = ["practice", "makes", "perfect", "coding", "makes"], "coding", "makes"

sl = Solution()
print( sl.shortestDistance( words, word1, word2 ) )