class Solution(object):
	# def __init__(self):
		# self.whatever = [1,2,3]


	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		# print(whatever)
		if digits == "":
			return []
		dic =  {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
		path = ""
		res = []
		def travel( digits, path, res):
			if digits == "":
				res.append( path )
				return 
			for i in dic[digits[0]]:
				travel( digits[1:], path+i, res )
			return
		travel(digits, path, res)
		return res



digits = "23"

sl = Solution()
print( sl.letterCombinations( digits ) )
