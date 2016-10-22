class Solution(object):
	def merge(self, nums1, m, nums2, n):
		"""
		:type nums1: List[int]
		:type m: int
		:type nums2: List[int]
		:type n: int
		:rtype: void Do not return anything, modify nums1 in-place instead.
		""" 
		nums1[:] = nums1[:m]
		nums2[:] = nums2[:n]
		for i in nums2:
			nums1.append( i )
			nums1.sort()
		# if m == 0:
		# 	nums1[:] = nums2
		# elif n == 0:
		# 	pass
		# else:
		   #  for i in nums2:
		   #  	nums1.append( i )
		   #  nums1.sort()



nums1, m = [1,0] , 1
nums2, n = [2] , 1

sl = Solution()
print( sl.merge(nums1, m , nums2, n) )
print( nums1 )