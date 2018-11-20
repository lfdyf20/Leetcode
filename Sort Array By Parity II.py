class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, 1
        while j < len(A):
            while i < len(A) and A[i] % 2 == 0:
                i += 2
            while j < len(A) and A[j] % 2 == 1:
                j += 2
            if j >= len(A):
                break
            A[i], A[j] = A[j], A[i]
            i += 2
            j += 2
        return A




A = [4,2,5,7]
A = [1, 2]
sl = Solution()
print( sl.sortArrayByParityII( A ) )