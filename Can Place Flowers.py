class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
        	if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
        		flowerbed[i] = 1
        		count += 1
        return count >= n



flowerbed, n = [0,0,1,0,0,0,1], 2

sl = Solution()
print( sl.canPlaceFlowers( flowerbed, n ) )