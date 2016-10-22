class Solution(object):
	def maxProduct(self, words):
	    """
	    :type words: List[str]
	    :rtype: int
	    """
	    words = sorted( words, key=lambda x: -len(x) )
	    maxValue = 0
	    for i in range( len(words)-1 ):
	    	# print( words[i] )
	    	for j in range( i+1, len(words) ):
	    		if self.compareStr( words[i], words[j] ):
	    			maxValue = max( len(words[i])*len(words[j]), maxValue)
	    			break
	    		else:
	    			pass
	    return maxValue


	def compareStr( self, str1, str2 ):
		for i in str1:
			if i in str2:
				return False
		return True
		





words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
sample = Solution()
print( sample.maxProduct( words ) )
# print( sample.compareStr( 'hello', 'w' ) )

