class Solution(object):
	def findMaximumXOR(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		answer = 0
		for i in range(32)[::-1]:
			answer <<= 1
			prefixes = {num >> i for num in nums}
			answer += any(answer^1 ^ p in prefixes for p in prefixes)
		return answer





nums = [3, 10, 5, 25, 2, 8]

sl = Solution()
print( sl.findMaximumXOR( nums ) )

"""
Build the answer bit by bit from left to right. 
For each bit try if it can be set. 
For example, let's say the answer so far is 0x10. 
Assume the next bit to the right is 1 - 0x101. 
Make a set S of all 3-bit prefixes of nums. 
If p1 and p2 are two prefixes from S and p1 ^ p2 = 0x101, then 0x101 ^ p1 = p2. 
By iterating over p1, we can check if 0x101 ^ p1 is also a prefix. 
If it is - then the rightmost bit can be 1, otherwise it is 0.
"""