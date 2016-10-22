class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """ 
        s = s.rstrip()
        chList = s.split(" ")
        res = len(chList[-1])
        return res




s = "a "
sample = Solution()
print(sample.lengthOfLastWord(s))


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
        	return root
        travel = []
        travel.append( (root, 'right', 0) )
        res = []
        index = -1
        
        while travel:
            currNode = travel.pop()
            node, label, level = currNode[0], currNode[1], currNode[2]
            if node.left:
            	travel.append( (node.left, 'left', level+1) )
            if node.right:
            	travel.append( (node.right, 'right', level+1) )
            if level > index:
            	res.append(node.val)
            	index += 1
        return res
            	