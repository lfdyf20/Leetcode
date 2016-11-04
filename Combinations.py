class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """ 
        # return [ [i] + p
        #     for i in range(1, n+1)
        #     for p in self.combine( i-1, k-1) ] or [[]]
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(1, n+1) for pre in self.combine(i-1, k-1)]


    def cb(self, n, k):
        def travel( k, nums, path ,res ):
            if k==0:
                if path not in res:
                    res.append( path )
                return
            if len(nums) < k:
                return 
            if len(nums) == k:
                res.append( path + nums )
                return
            travel( k, nums[1:], path, res )
            travel( k-1, nums[1:], path+[nums[0]], res)
            
        res = []
        nums = [i for i in range(1, n+1)]
        travel( k, nums, [], res )
        return res





n, k = 4, 2
n, k = 1, 0
sl = Solution()
print( sl.combine(n, k) )
print( sl.cb(n, k) )