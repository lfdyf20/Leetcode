class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        l, r = 0, n-1
        while l<=r:
        	mid = (l+r)//2
        	if citations[mid] >= n-mid:
        		r = mid - 1
        	else:
        		l = mid + 1
        return n-l






citations = [3,0,6,1,5,7,9,0,1,3,43,2,3]
citations = [0]
citations.sort()

sl = Solution()
print( sl.hIndex(citations) )

