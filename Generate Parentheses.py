# class Solution(object):

# 	def generateParenthesis(self, n):
# 		result = []
# 		self.dfs(n,result,'',0,0)
# 		return result

# 	def dfs(self,n,result,path,left,right):
# 		# check if the current path is valid
# 		if not self.isValid(left,right,n):
# 			return
# 		# check we are at the right length
# 		if len(path) == n*2:
# 			result.append(path)
# 			return
# 		self.dfs(n,result,path+'(',left+1,right)
# 		self.dfs(n,result,path+')',left,right+1)
		
# 	def isValid(self,left,right,n):
# 		# left paren <= right paren
# 		# left paren <= n
# 		# right paren >= n
# 		return left >= right and left <= n and right <= n

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.find( n, n, res )
        return list( set(res) )


    def find(self, n , N , res):
    	if n == 1:
    		return ['()']
    	resList = []
    	for i in self.find(n-1, N, res):
    		resList.append( i + '()' )
    		resList.append( '(' + i + ')' )
    		resList.append( '()' + i)
    	if n == N:
    		for i in resList:
    			res.append( i )
    	else:
    		return resList






n = 4
sl = Solution()
# print( sl.generateParenthesis(n) )
test = sl.generateParenthesis(n)
expected = ["(((())))","((()()))","((())())",
			"((()))()","(()(()))","(()()())",
			"(()())()","(())(())","(())()()",
			"()((()))","()(()())","()(())()",
			"()()(())","()()()()"]
for i in expected:
	if i not in test:
		print(i)