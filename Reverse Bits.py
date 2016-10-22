class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
    	return int(bin(n)[2:].zfill(32)[::-1], 2)



n = 43261596

sl = Solution()
print( sl.reverseBits( n ) )