class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1, l2 = len(num1), len(num2)
        if l1 < l2:
        	return self.addStrings(num2, num1)

        print( num1[:l1-l2] )

        if not num2 or num2 == '0':
        	return num1

        res = ''
        carry = 0
        for i in range(l2):
        	tempSum = carry + int(num1[~i]) + int(num2[~i])
        	res = str( tempSum%10 ) + res
        	carry = tempSum//10
        
        if carry == 0:
        	res = num1[:l1-l2] + res
        else:
        	res = self.addStrings(num1[:l1-l2], '1') + res

        return res




num1, num2 = "123", "11789"
# num1, num2 = '99', '9'

sl = Solution()
print( sl.addStrings( num1, num2 ) )