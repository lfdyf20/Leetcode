class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse = True)
        print(citations)
        res = 0
        for i in range(len(citations)):
        	if citations[i] >= i+1:
        		res = i+1
        return res

    def hi(self, citations):
        citations.sort(reverse = True)
        for i, num in enumerate( citations ):
            if num == i+1:
                return i+1
            if num < i+1:
                return i
        else:
            return len(citations)

    def h(self, citations):
        return sum(i < j for i, j in enumerate(sorted(citations, reverse=True)))



citations = [3,0,6,1,5,7,9,0,1,3,43,2,3]
# citations = [2,1]
# citations = [3, 0, 6, 1, 5]
# citations = [100]

sl = Solution()
print( sl.hIndex( citations ) )
print( sl.h(citations) )