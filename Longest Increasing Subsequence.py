class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        # maxVal = 0
        # count = [1]*len(nums)
        # for i in range( len(nums) ):
        # 	for j in range(0,i):
        # 		if nums[j]<nums[i]:
        # 			count[i] = max( count[i], count[j]+1 )
        # 	maxVal = max( count[i], maxVal )
        # print(count)
        # return maxVal
        count = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    count[i] = max(count[i], count[j]+1)
        return max(count) if count else 0

    def my(self, nums):
        res = []
        for num in nums:
            print(res)
            if res == [] or num > res[-1]:
                res += [ num ]
                continue
            for i in range(len(res)):
                if num <= res[~i]:
                    while i<len(res) and num <= res[~i]: 
                        i += 1
                    res[~i+1] = num
                    break
        print(res)
        return len(res)

    def nlogn(self, nums):
        res = []
        for num in nums:
            print(res)
            if res == [] or num > res[-1]:
                res += [ num ]
                continue
            l, r = 0, len(res)
            while l < r:
                mid = (l+r)//2
                if res[mid] < num:
                    l = mid+1
                else:
                    r = mid
            res[l] = num 
        print(res)
        return len(res)




nums = [10, 9, 2, 5, 3, 7, 101, 18]
nums = [3,1,4,5,9,2,6]
# nums = []
# nums = [1,2]
# nums = [4,10,4,3,8,9]
sl =Solution()
print( sl.lengthOfLIS(nums) )
print( sl.my(nums) )
print( sl.nlogn(nums) )