class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        # calculate period
        p = 2*(numRows-1)

        res = [""] * numRows
        for i in xrange(len(s)):
            print "i=",i
            floor = i%p
            print "floor is:",floor
            if floor >= p/2:
                floor = p - floor
                print "here floor is: ",floor
            res[floor] += s[i]
            print res
        return "".join(res)



s = "PAYPALISHIRING"
numRows = 3

sample = Solution()
print sample.convert(s, numRows)

