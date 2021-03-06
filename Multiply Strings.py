class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0]*(len(num1)+len(num2))
        for i, e1 in enumerate(reversed(num1)):
        	for j, e2 in enumerate(reversed(num2)):
        		res[i+j] += int(e1) * int(e2)
        		res[i+j+1] += res[i+j] // 10
        		res[i+j] = res[i+j] % 10
        print(res)
        while len(res) > 1 and res[-1] == 0:
        	res.pop()
        return "".join(map(str, res[::-1])) if len(res) > 0 else '0'






num1, num2 = "1", "1"

sl = Solution()
print( sl.multiply( num1, num2 ) )