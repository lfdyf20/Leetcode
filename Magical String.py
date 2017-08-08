class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        queue = [1,2,2]
        i = 2
        while len(queue) < n:
        	queue += queue[i] * [3-queue[-1]]
        	i += 1
        return queue[:n].count(1)



n = 5

sl = Solution()
print( sl.magicalString( n ) )