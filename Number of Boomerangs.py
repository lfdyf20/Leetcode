from itertools import combinations
from collections import defaultdict
import collections
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        return sum(
        n * (n - 1)
        for x1, y1 in points
        for n in collections.Counter(
            (x1 - x2) ** 2 + (y1 - y2) ** 2
            for x2, y2 in points).values())

    #     if len(points) < 3:
    #     	return 0
    #     dic = defaultdict( lambda :defaultdict(int) )
    #     for p1, p2 in combinations( points, 2 ):
    #     	dis = self.dis(p1, p2)
    #     	dic[tuple(p1)][dis] += 1
    #     	dic[tuple(p2)][dis] += 1
    #     res = 0
    #     for point, pdict in dic.items():
    #     	for dis, count in pdict.items():
    #     		if count > 1:
    #     			res += count * (count-1)
    #     return res



    # def dis(self, p1, p2):
    # 	x1, y1 = p1
    # 	x2, y2 = p2
    # 	return (x1-x2)**2 + (y1-y2)**2



points = [[0,0],[1,0],[2,0], [1,1]]

sl = Solution()
print( sl.numberOfBoomerangs( points ) )