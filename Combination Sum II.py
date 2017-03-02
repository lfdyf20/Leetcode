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

    def mySolution(self, candidates, target):
        def travel(candidates, start, target, res, path ):
            # print(candidates, start, res)
            if target < 0:
                return
            if target == 0:
                res.append( path )
                return
            if not candidates:
                return
            for i in range(start, len(candidates)):
                if start != i and candidates[i] == candidates[i-1]:
                    continue
                travel(candidates, i+1, target-candidates[i], res, path+[candidates[i]])
            # return res

        candidates.sort(reverse=True)
        res = []
        travel(candidates, 0, target, res, [])
        return res






candidates, target = [10, 1, 1, 2, 7, 6, 5], 8


sl = Solution()
print( sl.combinationSum2( candidates, target ) )
print( sl.mySolution(candidates, target) )