class Solution(object):
	def combinationSum(self, candidates, target):
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		path = []
		res = []
		self.helpCom( candidates,target,path,res )
		return res


	def helpCom(self, candidates, target, path, res):
		updatePath = []
		if target < 0:
			return
		if target == 0:
			res.append(path)
			return
		if candidates == []:
			return
		self.helpCom( candidates[1:], target, path, res )
		self.helpCom( candidates, target-candidates[0], path+[candidates[0]], res )

	def mySolution(self, candidates, target):

		def travel(candidates, target, path, res):
			if target < 0:
				return
			if target == 0:
				res.append( path )
				return
			if not candidates:
				return
			travel( candidates, target-candidates[0], path+[candidates[0]], res )
			travel( candidates[1:], target, path, res )

		res = []
		travel( candidates, target, [], res )
		return res



candidates = [2,3,6,7]
target = 7
sl = Solution()
print( sl.combinationSum(candidates,target) )
print( sl.mySolution(candidates, target) )