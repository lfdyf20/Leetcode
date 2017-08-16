class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x:(x[0], -x[1]))
        print(points)
        count = 0
        preR = float('-inf')
        for l,r in points:
        	if l > preR:
        		count += 1
        		preR = r
        		continue
        	if r < preR:
        		preR = r
        return count


    # better: different way to sort the array, make it more effective to go through
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points, key = lambda x: x[1])
        res, end = 0, -float('inf')
        for interval in points:
            if interval[0] > end:
                res += 1
                end = interval[1]
        return res


points = [[10,16], [2,8], [1,6], [7,12]]
# points = []
# points = [[1,4]]
# points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]

sl = Solution()
print( sl.findMinArrowShots( points ) )