class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        for left, right in zip( [lower-1] + nums, nums + [upper+1] ):
        	left, right = left + 1, right -1
        	if right == left:
        		res.append( str(left) )
        	elif right > left:
        		res.append( "{}->{}".format( left, right ) )
        return res
        



nums, lower, upper = [0, 1, 3, 50, 75], 0, 75

sl = Solution()
print( sl.findMissingRanges( nums, lower, upper ) )