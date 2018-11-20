class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                return i
        else:
            return len(A)-1

    def binarySearch(self, A):
        l, r = 0, len(A) - 1
        while l < r:
            mid = (l + r) // 2
            if A[mid] < A[mid+1]:
                l = mid
            elif A[mid] < A[mid-1]:
                r = mid
            else:
                return mid



A = [0,2,1,0]
# A = [2,3,4]
# A = [4,3,2]

sl = Solution()
print( sl.peakIndexInMountainArray( A ) )
print( sl.binarySearch(A) )