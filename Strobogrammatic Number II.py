class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.dic = {1:1, 6:9, 9:6, 8:8, 0:0}
        self.res = []        

        def travel(n, left, right):
        	if n==0:
        		res = left + right
        		self.res.append( res )
        		return
        	if n==1:
        		for i in ["1", "8", "0"]:
        			res = left + i + right
        			self.res.append( res )
        		return
        	for i in self.dic:
        		if left == "" and i == 0:
        			continue
        		travel( n-2, left+str(i), str(self.dic[i])+right )
        	return

        travel(n,"", "")
        return self.res 


    def online(self, n):
	    nums = n%2 * list('018') or ['']
	    while n > 1:
	        n -= 2
	        nums = [a + num + b for a, b in '00 11 88 69 96'.split()[n<2:] for num in nums]
	    return nums


n = 3

sl = Solution()
print( sl.findStrobogrammatic( n ) )