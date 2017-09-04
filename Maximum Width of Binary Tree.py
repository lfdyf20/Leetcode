class Solution(object):
	def widthOfBinaryTree(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		stack, res = [root], 0
		while stack:
			temp = []
			res = max(len(stack), res)
			for node in stack:
				if node:
					temp += [node.left, node.right]
				elif temp:
					temp += [None, None]
			while temp and temp[-1] == None:
				temp.pop()
			stack = temp
			for i in range(len(stack)):
				if stack[i] != None:
					stack = stack[i:]
					break
		return res


	def widthOfBinaryTree(self, root):
	    queue = [(root, 0, 0)]
	    cur_depth = left = ans = 0
	    for node, depth, pos in queue:
	        if node:
	            queue.append((node.left, depth+1, pos*2))
	            queue.append((node.right, depth+1, pos*2 + 1))
	            if cur_depth != depth:
	                cur_depth = depth
	                left = pos
	            ans = max(pos - left + 1, ans)

	    return ans


vals = '[1,3,2,5,3,null,9]'
# vals = '[1,2,3,4,null,null,7,8,null,null,11]'
vals= '[1,3,2,5]'
vals = '[1,1,1,1,1,1,1,null,null,null,1,null,null,null,null,2,2,2,2,2,2,2,null,2,null,null,2,null,2]'
# vals = '[1,null,2]'


from Tree import BinaryTree 
t = BinaryTree(vals)
# print(t)

root = t.getRoot()

sl = Solution()
print( sl.widthOfBinaryTree( root ) )