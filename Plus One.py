class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int(''.join(map(str,digits))) + 1
        res = list( map( int , str(num) ) )
        return res






digits = [1,2,4,9,9]
sample = Solution()
print sample.plusOne(digits) 
print type(''.join( map(str, digits) ))