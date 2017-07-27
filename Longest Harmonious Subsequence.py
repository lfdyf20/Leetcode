class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic_list = {}
        for num in nums:
        	for i in num+0.5, num-0.5, :
        		if i in dic_list:
        			dic_list[i].append(num)
        		else:
        			dic_list[i] = [num]
        lists = [len(li) for li in dic_list.values() if max(li)-min(li)==1]
        return max(lists) if lists else 0


    def online(self, nums):
    	count = {}
    	for i in nums:
    		count[i] = count.get(i,0) + 1
    	return max( count[i] + count[i+1] if i+1 in count else 0 for i in count) if nums else 0
        



nums = [1,3,2,2,5,2,3,7]
nums = []
# nums = [1,1,1,1]

sl = Solution()
print( sl.findLHS( nums ) )
print( sl.online(nums) )