class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        S = {-1: set()}
        for i in sorted(nums):
        	S[i] = max( (S[k] for k in S if i%k == 0), key=len )|{i}
        print( S )
        return list(max(S.values(), key=len))


        # if nums == []:
        # 	return []
        # nums.sort()
        # comb = []
        # for i in nums:
        # 	if comb == []:
        # 		comb.append([i])
        # 		continue
        # 	temp = []
        # 	for j in comb:
        # 		if i % j[-1] ==0:
        # 			temp.append(j+[i])
        # 	comb += temp
        # 	comb.append([i])
        # return max(comb, key = len)


nums = [3,4,12,16,8]
sl = Solution()
print( sl.largestDivisibleSubset(nums) )