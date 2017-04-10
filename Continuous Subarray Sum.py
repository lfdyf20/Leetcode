class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """ 
        k = abs(k)
        if k == 1:
        	return len(nums)>=2
        if k == 0:
            return '00' in ''.join( list(map(str, nums)) )
        record = set()
        for num in nums:
        	if num%k in record:
        		return True
        	temp = set([k-num%k])
        	if num == 0:
        		temp.add(num)
        	for i in record:
        		if i > num%k:
        			temp.add( i-num%k )
        		else:
        			temp.add( abs(k-(num%k-i)%k) )
        	# print(num, record, temp)
        	record = temp
        	
        return False
        


tests = [
	([0,1,0], -1),
	([23, 2, 6, 4, 7], 6),
	([4,0],1),
	([1,2,3],6),
	([3,5],6),
]

sl = Solution()

for nums, k in tests:
	print('{2} \t[nums={0},k={1}]'.format(nums,k, sl.checkSubarraySum( nums, k )))
