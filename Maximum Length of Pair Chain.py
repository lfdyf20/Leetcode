class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda pair:pair[1])
        print(pairs)
        pre, count = float('-inf'), 0
        for l, r in pairs:
        	if l > pre:
        		pre = r
        		count += 1
        return count


pairs = [[1,2], [2,3], [3,4]]

sl = Solution()
print( sl.findLongestChain( pairs ) )