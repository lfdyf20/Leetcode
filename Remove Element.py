class Solution(object):
		def removeElement(self, nums, val):
				"""
				:type nums: List[int]
				:type val: int
				:rtype: int
				"""
				# nums.sort()
				# length = 0
				# for i in range( len(nums) ):
				# 	if nums[i] == val:
				# 		del nums[i]
				# 		length += 1
				# 		nums.insert(0, 'bingo')
				# nums.reverse()
				# return len(nums)-length
				nums.sort( key = lambda x: x==val)

				print(nums)



nums = [3,2,2,3]
val = 3
sample = Solution()
print(sample.removeElement(nums,val)) 
print(nums)