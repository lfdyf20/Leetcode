class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        stack, res = [], 0
        for num in nums:
        	d, p, v = num//100, num%100//10, num%10
        	dict[ (d,p) ] = v
        	if (d,p) == (1,1):
        		stack.append( (d,p,v) )
        
        while stack:
        	cd, cp, cv = stack.pop()
        	if (cd+1, cp*2-1) not in dict and (cd+1, cp*2) not in dict:
        		res += cv
        		continue
        	if (cd+1, cp*2-1) in dict:
        		stack.append( (cd+1, cp*2-1, cv + dict[(cd+1, cp*2-1)]) )
        	if (cd+1, cp*2) in dict:
        		stack.append( (cd+1, cp*2, cv + dict[(cd+1, cp*2)]) )


        return res





nums = [113, 215, 221]
nums = [113, 221]
nums = []

sl = Solution()
print( sl.pathSum( nums ) )