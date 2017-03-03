import re
class Solution(object):
	def simplifyPath(self, path):
		"""
		:type path: str
		:rtype: str
		"""
		
		stack = []
		for token in path.split('/'):
			if token in ('', '.'):
				pass
			elif token == '..':
				if stack: stack.pop()
			else:
				stack.append(token)
		return '/' + '/'.join(stack)


	def mySolution(self, path):
		stack = []
		for i in path.split('/'):
			if i in ['', '.']:
				pass
			elif i == '..':
				if stack:
					stack.pop()
			else:
				stack.append( i )
		return '/'+'/'.join( stack )
		
		




path = "/a/./b/../../c/"
# path = "/home/"
# # path = "///"
# # path = "/..."
# # path = "//"
# # path = "/.../"
path = "/abc/..."

sl = Solution()
print( sl.simplifyPath( path ) )
print( sl.mySolution(path) )