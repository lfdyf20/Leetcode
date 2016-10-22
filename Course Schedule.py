import collections
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        csDic = {i : set() for i in range(numCourses)}
        preDic = collections.defaultdict( set )
        for cs, pre in prerequisites:
        	csDic[cs].add( pre )
        	preDic[pre].add( cs )
        print(csDic)
        print(preDic)
        canLearn = collections.deque()
        for i in csDic:
        	if not csDic[i]:
        		canLearn.append(i)
        if not canLearn:
        	return False
        count = 0
        while canLearn:
        	learnedPre = canLearn.popleft()
        	count += 1
        	if count >= numCourses:
        		return True
        	for cs in preDic[learnedPre]:
        		csDic[cs].remove( learnedPre )
        		if not csDic[cs]:
        			canLearn.append(cs)
        return False




numCourses = 2
prerequisites = [[1,0]]

sl = Solution()
print( sl.canFinish( numCourses, prerequisites ) )