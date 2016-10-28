class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1] * len(nums)
        for i in range( 1, len(nums) ):
            left[i] = left[i-1]*nums[i-1]
        # print(left)
        right = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        # print(right)
        res = []
        for i,j in zip(left, right):
            res.append(i*j)
        return res
        



    # # @param {integer[]} nums
    # # @return {integer[]}
    # def productExceptSelf(self, nums):
    #     # p = 1
    #     # n = len(nums)
    #     # output = []
    #     # for i in range(n):
    #     #     output.append(p)
    #     #     p = p * nums[i]
    #     # p = 1
    #     # print("1 output: ", output)
    #     # for i in range(n-1,-1,-1):
    #     #     output[i] = output[i] * p
    #     #     p = p * nums[i]
    #     # return output




nums = [1,2,3,4]
# print(nums)
sl = Solution()
print( sl.productExceptSelf(nums) ) 