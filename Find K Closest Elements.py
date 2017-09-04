class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        arr.sort(key=lambda a:(abs(a-x), a-x))
        return sorted(arr[:k])

    def binarySearch(self, arr, k, x):
    	from bisect import bisect_left
    	left = right = bisect_left(arr, x)
    	while right - left < k:
    		if left == 0: return arr[:k]
    		if right == len(arr): return arr[-k:]
    		if x - arr[left-1] <= arr[right] - x: left += 1
    		else:	right += 1
    	return arr[left: right]
        



arr, k, x = [1,2,3,4,5], 4, -1

sl = Solution()
print( sl.findClosestElements( arr, k, x ) )