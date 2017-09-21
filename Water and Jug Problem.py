class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        gcd, r = max(x, y), min(x, y)
        while r:
        	gcd, r = r, gcd % r
        return z == 0 or x + y >= z and z%gcd == 0



x, y, z = 4,8,2

sl = Solution()
print( sl.canMeasureWater( x, y, z ) )