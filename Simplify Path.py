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
		
		# match1 = re.search("(\/\w*)\/$", path)
		# if match1:
		# 	res = match1.group(1)
		# 	return res
		# match2 = re.search( "(\/\.\.\.)\/?$", path)
		# if match2:
		# 	res = match2.group(1)
		# 	return res
		# return "/"




path = "/a/./b/../../c/"
# path = "/home/"
# # path = "///"
# # path = "/..."
# # path = "//"
# # path = "/.../"
path = "/abc/..."

sl = Solution()
print( sl.simplifyPath( path ) )