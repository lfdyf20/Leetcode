class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
    	a = s.split()
    	return " ".join(a[::-1])


s = "the sky is blue"

sl = Solution()
print( sl.reverseWords( s ) )

grid = [[1,2,3],[2,3,4]]
