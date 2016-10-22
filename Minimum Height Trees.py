import collections
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 0:
        	return [0]
        flag = 0
        res = set()
        distDic = collections.defaultdict( set )
        for i, j in edges:
        	distDic[i].add(j)
        	distDic[j].add(i)
        count = 1
        print( distDic )
        backDic = distDic.copy()
        while True and count < 1000:
        	count += 1
  	
        	for i, nebs in distDic.items() :
        		if len(distDic[i]) == n-1:
        			flag = 1
        			res.add(i)
        		nebSet = set()
        		for neb in nebs:
        			nebSet = nebSet | backDic[ neb ]
        		distDic[i] = distDic[i] | nebSet - set( [i] )
       
        	if flag == 1:
        		print(distDic, count)
        		return list( res ) 
        	backDic = distDic.copy()


        # for i, j in edges:
        # 	distDic[i][j] = 1
        # 	distDic[j][i] = 1
        # print(distDic)
        # for i, nebs in distDic.items():
        # 	print(i, neb)
        # 	for neb in nebs:
        # 		for  



n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

n = 4
edges = [[1,0],[1,2],[1,3]]

n = 7
edges = [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]]

sl = Solution()
print( sl.findMinHeightTrees( n, edges ) )