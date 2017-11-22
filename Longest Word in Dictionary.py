class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        visited = {''}
        for word in sorted(words):
        	if word[:-1] in visited:
        		visited.add(word)
        return max( sorted(visited), key=len )





words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]

sl = Solution()
print( sl.longestWord( words ) )