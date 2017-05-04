class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l, r = 0, num//2+1

        while l <= r:
        	mid = (l+r)//2
        	midVal = mid**2
        	if midVal == num:
        		return True
        	elif midVal < num:
        		l = mid + 1
        	else:
        		r = mid - 1
        return False

    def online1(self, num):
    	i = 1
    	res = 0
    	while res < num:
    		res += i
    		i += 2
    	return res==num or num==0

nums = [0,1,2,3,4,5,6,16,100,1001]

sl = Solution()

for num in nums:
	print( "{} is {}".format(num, sl.isPerfectSquare( num )) )
	print( "{} is {}".format(num, sl.online1( num )) )