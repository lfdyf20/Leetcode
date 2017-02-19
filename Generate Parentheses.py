import time
class Solution(object):

	def generateParenthesis(self, n):
		result = []
		self.dfs(n,result,'',0,0)
		return result

	def dfs(self,n,result,path,left,right):
		# check if the current path is valid
		if not self.isValid(left,right,n):
			return
		# check we are at the right length
		if len(path) == n*2:
			result.append(path)
			return
		self.dfs(n,result,path+'(',left+1,right)
		self.dfs(n,result,path+')',left,right+1)
		
	def isValid(self,left,right,n):
		return left >= right and left <= n and right <= n


	def muSolution(self, n):
		stack = [('',0,0)]
		for i in range(n*2):
			curr = []
			while stack:
				pre, l, r = stack.pop()
				if l<r:
					continue
				elif l > n or r > n:
					continue   
				elif l==n and r<n:
					curr.append( (pre+')', l, r+1) )     
				elif l==r:
					curr.append( (pre+'(', l+1, r) )
				else:
					curr += [ (pre+'(',l+1,r), (pre+')',l,r+1) ]
			stack = curr[:]
		res = list(map(lambda x:x[0], stack))
		return res



# class Solution(object):
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         res = []
#         self.find( n, n, res )
#         return list( set(res) )


#     def find(self, n , N , res):
#     	if n == 1:
#     		return ['()']
#     	resList = []
#     	for i in self.find(n-1, N, res):
#     		resList.append( i + '()' )
#     		resList.append( '(' + i + ')' )
#     		resList.append( '()' + i)
#     	if n == N:
#     		for i in resList:
#     			res.append( i )
#     	else:
#     		return resList






n = 10
sl = Solution()
start1 = time.time()
print( len(sl.generateParenthesis(n)))
print(time.time()-start1)

start2 = time.time()
print( len(sl.muSolution(n)) )
print( time.time()-start2 )
# test = sl.generateParenthesis(n)
# expected = ['(()()())', '()()(())', '()()()()', '((()()))', '(()())()', '((()))()', '()(())()', '((())())', '()((()))', '(()(()))', '(((())))', '()(()())', '(())()()']
# for i in expected:
# 	if i not in test:
# 		print(i)