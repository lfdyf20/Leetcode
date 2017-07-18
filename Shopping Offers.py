class Solution(object):
	def shoppingOffers(self, price, special, needs):
		"""
		:type price: List[int]
		:type special: List[List[int]]
		:type needs: List[int]
		:rtype: int
		""" 
		dic = {}
		def dfs(curr_needs):
			res = sum(need * p for need, p in zip(curr_needs, price))
			for offer in special:
				temp_needs = [ need - buy for need, buy in zip(curr_needs, offer) ]
				if min(temp_needs) >= 0:
					res = min(res, dic.get(tuple(temp_needs), dfs(temp_needs))+offer[-1])
			dic[ tuple(curr_needs) ] = res
			return res
		return dfs(needs)       		



price, special, needs = [2,5], [[3,0,5],[1,2,10]], [3,2]

sl = Solution()
print( sl.shoppingOffers( price, special, needs ) )