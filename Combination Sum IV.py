class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = [1]
        nums.sort()
        for i in range(1, target+1):
            amount = 0
            for num in nums:
                if num > i:
                    break
                amount += count[i-num]
    
            count.append(amount)
        return count[-1]

    def cs(self, nums, target):
        def travel( target, nums, path, res ):
            if target == 0:
                res.append( path )
                return
            if nums == []:
                return
            if target < 0 or target < nums[0]:
                return
            for i in range(len(nums)):
                travel( target-nums[i], nums, path+[nums[i]], res )
            return
        
        res = []
        travel( target, nums, [], res )
        return res

    def mySolution(self, nums, target):
        nums, combos = sorted(nums), [1]+[0]*target
        for i in range(1, target+1):
            for num in nums:
                if num > i: break
                combos[i] += combos[i-num]
        return combos[-1]




nums = [3,1,2,4]
target = 4
sl = Solution()
print( sl.combinationSum4( nums, target ) )
print( sl.cs(nums, target) )
print( sl.mySolution(nums, target) )