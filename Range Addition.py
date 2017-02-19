class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        res = [0] * length
        for start, end, update in updates:
        	res[start: end+1] = [i+update for i in res[start: end+1]]
        return res

    def mySolution(self, length, updates):
        res = [0] * (length+1)
        for start, end, update in updates:
            res[start] += update
            res[min(end+1, length)] -= update
        carry = 0
        for i in range( length ):
            carry, res[i] = carry+res[i], carry+res[i]
            # carry += res[i]
            # res[i] = carry
        return res[:-1]


length = 5
updates = [
        [1,  3,  2],
        [2,  4,  3],
        [0,  2, -2]
    ]

sl = Solution()
print( sl.getModifiedArray( length, updates ) )