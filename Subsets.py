class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """ 
        subset = [[]]
        for i in nums:
        	temp = []
        	for j in subset:
        		temp.append(j+[i])
        	subset = subset + temp
        return subset

    def mySolution( self, nums ):
        res = [[]]
        for i in nums:
            res += [ pre + [i] for pre in res ]
        return res

        


nums = [1,2,3]
sl =Solution()
print( sl.subsets(nums) )
print( sl.mySolution(nums) )