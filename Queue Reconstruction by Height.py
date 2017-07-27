class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda p:(-p[0],p[1]))
        # print(people)
        res = []
        for p in people:
        	res.insert(p[1], p)
        return res



people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

sl = Solution()
print( sl.reconstructQueue( people ) )