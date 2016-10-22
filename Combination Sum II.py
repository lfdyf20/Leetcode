class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort(reverse = True)
        print(candidates)
        res = []
        path = []
        self.travel(candidates, target, path, res)
        return res

    def travel( self, candidates, target, path, res ):
        	if target == 0:
        		if path not in res:
        			res.append(path)
        		return
        	if target < 0:
        		return
        	if candidates == []:
        		return
    
        	self.travel(candidates[1:], target - candidates[0], path+[candidates[0]], res)
        	self.travel(candidates[1:], target , path, res)





candidates, target = [10, 1, 1, 2, 7, 6, 5], 8


sl = Solution()
print( sl.combinationSum2( candidates, target ) )