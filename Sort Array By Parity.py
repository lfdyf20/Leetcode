class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted(A, key=lambda x:x%2)
        


A = [3,1,2,4]

sl = Solution()
print( sl.sortArrayByParity( A ) )