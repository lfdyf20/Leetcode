class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """ 
        for i in range(len(words)):
            for j in range(i+1 ,len(words[i])):
                if j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
        return True


words = ["ball","area","read","lady"]

sl = Solution()
print( sl.validWordSquare( words ) )