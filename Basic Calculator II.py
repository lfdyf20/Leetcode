from math import floor
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        operators = ["-","+","*","/"]
        stack = []
        stack0 = []
        for i in s:
        	if not stack0:
        		stack0.append(i)
        	elif i.isdigit():
        		temp = stack0.pop()
        		if temp.isdigit():
        			stack0.append(temp+i)
        		else:
        			stack0.append(temp)
        			stack0.append(i)
        	else:
        		stack0.append(i)

        # print(stack0)
        for i in stack0:
        	if i == " ":
        		continue
        	elif i in operators:
        		stack.append(i)
        	else:
        		if not stack:
        			stack.append(i)
        			continue
        		temp = stack.pop()
        		if temp.isdigit():
        			stack.append( temp+i )
        		elif temp == "+" or temp == "-":
        			stack.append(temp)
        			stack.append(i)
        		else:
        			x, y, f = stack.pop(), i, temp
        			stack.append( self.compute(x,y,f) )
        # print(stack)
        op = ""
        val = 0
        for i in stack:
        	if i.isdigit():
        		if op == "":
        			val = int(i)
        			continue
        		if op == "-":
        			val -= int(i)
        			continue
        		if op == "+":
        			val += int(i)
        			continue
        	else:
        		op = i

        return val

    def compute(self, x, y, f ):
    	if f == "-":
    		return str(int(x) - int(y))
    	elif f == "+":
    		return str(int(x) + int(y))
    	elif f == "*":
    		return str(int(x) * int(y))
    	elif f == "/":
    		return str(floor(int(x) / int(y)))
    	else:
    		return "error"


    def calculate2(self, s):
	    if not s:
	        return "0"
	    stack, num, sign = [], 0, "+"
	    for i in range(len(s)):
	        if s[i].isdigit():
	            num = num*10+ord(s[i])-ord("0")
	        if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
	            if sign == "-":
	                stack.append(-num)
	            elif sign == "+":
	                stack.append(num)
	            elif sign == "*":
	                stack.append(stack.pop()*num)
	            else:
	                tmp = stack.pop()
	                if tmp//num < 0 and tmp%num != 0:
	                    stack.append(tmp//num+1)
	                else:
	                    stack.append(tmp//num)
	            sign = s[i]
	            num = 0
	    return sum(stack)








sl = Solution()
S = ["3*2+4/2", "0/1", "0*1", "2/2/3", "2+4*12-43","14/3*2"]
for s in S:
	my = sl.calculate(s)
	his = sl.calculate2(s)
	print( my == his, my, his )
# s = "2+4*12-43"
# print(s)
# print( sl.calculate(s) )


