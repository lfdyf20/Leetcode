class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        numsstr = list(str(num))
        for i, x in enumerate(sorted(numsstr, reverse=True)):
        	if x > numsstr[i]:
        		pre, numsstr[i] = numsstr[i], x
        		break
        else:
        	return num
        for i in range(len(numsstr)):
        	if numsstr[~i] == x:
        		numsstr[~i] = pre
        		break
        return eval("".join(numsstr))

        	




num = 9973

sl = Solution()
print( sl.maximumSwap( num ) )