class Solution(object):
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        total = sum( abs(x-tree[0]) + abs(y-tree[1]) for x,y in nuts ) * 2
        dis = min( [(abs(squirrel[0]-x) + abs(squirrel[1]-y), abs(x-tree[0]) + abs(y-tree[1])) for x, y in nuts], key=lambda d:d[0]-d[1]  )
        return total + dis[0] - dis[1]



height = 5
width = 7
tree = [2,2]
squirrel = [4,4]
nuts = [[3,0], [2,5]]
height = 5
width = 5
tree = [3,2]
squirrel = [0,1]
nuts = [[2,0],[4,1],[0,4],[1,3],[1,0],[3,4],[3,0],[2,3],[0,2],[0,0],[2,2],[4,2],[3,3],[4,4],[4,0],[4,3],[3,1],[2,1],[1,4],[2,4]]

sl = Solution()
print( sl.minDistance( height, width, tree, squirrel, nuts ) )