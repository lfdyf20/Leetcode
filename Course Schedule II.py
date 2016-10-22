import collections
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        csDic = {i: set() for i in range(numCourses)}
        preDic = collections.defaultdict( set )
        for cs, pre in prerequisites:
        	csDic[cs].add( pre )
        	preDic[pre].add( cs )
        print(csDic)
        print(preDic)
        learned = collections.deque( [cs for cs in csDic if not csDic[cs] ] )
        print(learned)

        count, res = 0, []
        while learned:
        	learnedCs = learned.popleft()
        	res.append( learnedCs )
        	count += 1
        	for cs in preDic[ learnedCs ]:
        		csDic[cs].remove(learnedCs)
        		if not csDic[cs]:
        			learned.append(cs)

        return res if len(res) == numCourses else []






        



numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

sl = Solution()
print( sl.findOrder( numCourses, prerequisites ) )


a = set( [1,2,3,4] )
b = set( [1,2] )
print( b <= a )