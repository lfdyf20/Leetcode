class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse = True)
        # print(citations)
        res = 0
        for i in range(len(citations)):
        	if citations[i] >= i+1:
        		res = i+1
        return res




citations = [3,0,6,1,5,7,9,0,1,3,43,2,3]

sl = Solution()
print( sl.hIndex( citations ) )