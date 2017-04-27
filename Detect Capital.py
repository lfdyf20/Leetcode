class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        count = 0
        n = len(word)
        for i in word:
        	if i.isupper():
        		count += 1
        return (count==1 and word[0].isupper()) or count==n or count==0



word = 'A'

sl = Solution()
print( sl.detectCapitalUse( word ) )