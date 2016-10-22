from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        count = 0
        cs_pre = defaultdict(list)
        pre_cs = defaultdict(list)
        for cs, pre in prerequisites:
        	cs_pre[cs].append( pre )
        	pre_cs[pre].append( cs )
        





numCourses, prerequisites = 2, [[1,0],[0,1]]

sl = Solution()
print( sl.canFinish( numCourses, prerequisites ) )


print( "hi, world" )