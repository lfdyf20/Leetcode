class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """ 
        stack = []
        point = ""
        for i in s:
        	if i =="(":
        		stack.append(i)
        	elif i == "[":
        		stack.append(i)
        	elif i == "{":
        		stack.append(i)
        	elif i == ")":
        		if len(stack)==0:
        			return False
        		j = stack.pop()
        		if j != "(":
        			return False
        	elif i == "]":
        		if len(stack)==0:
        			return False
        		j = stack.pop()
        		if j != "[":
        			return False
        	elif i == "}":
        		if len(stack)==0:
        			return False
        		j = stack.pop()
        		if j != "{":
        			return False
        if len(stack)>0:
        	return False


        return True








s = "}"
sample = Solution()
print sample.isValid(s)