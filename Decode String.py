import re

class Solution(object):
	def decodeString(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		while '[' in s:
			s = re.sub(r'(\d+)\[(\w*)\]', lambda x: int(x.group(1)) * x.group(2), s)
		return s


# anothe solution
# class Solution(object):
#     def decodeString(self, s):
#         stack = []
#         stack.append(["", 1])
#         num = ""
#         for ch in s:
#             if ch.isdigit():
#               num += ch
#             elif ch == '[':
#                 stack.append(["", int(num)])
#                 num = "" 
#             elif ch == ']':
#                 st, k = stack.pop()
#                 stack[-1][0] += st*k
#             else:
#                 stack[-1][0] += ch
#         return stack[0][0]



s = "3[a]2[bc]"
s = '3[a2[c]]'
# s = "2[abc]3[cd]ef"

sl = Solution()
print( sl.decodeString(s) )
# print( 3*s )
