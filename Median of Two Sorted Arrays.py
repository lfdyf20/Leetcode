# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         l = len(nums1) + len(nums2)
#         if l%2:
#         	return self.findKthSmallest(nums1, nums2, l//2+1)
#         else:
#         	return ( self.findKthSmallest(nums1. nums2, l//2) + 
#         		self.findKthSmallest(nums1, nums2, l//2+1)/2)

#     def findKthSmallest(self, nums1, nums2, k):
#     	if len(nums1) > len(nums2):
#     		return self.findKthSmallest(nums2, nums1, k)
#     	if not nums1:
#     		return nums2[k-1]
#     	if k==1:
#     		return min(nums1[0], nums2[0])
#     	pa = min(k//2, len(nums1))
#     	pb = k-pa
#     	if nums1[pa-1] <= nums2[pb-1]:
#         	return self.findKthSmallest(nums1[pa:], nums2, k-pa)
#     	else:
#         	return self.findKthSmallest(nums1, nums2[pb:], k-pb)

class Solution(object):
	def findMedianSortedArrays(self, A, B):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""
	 
		l = len(A) + len(B)
		if l % 2 == 1:
			return self.kth(A, B, l // 2)
		else:
			return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.   
	
	def kth(self, a, b, k):
		if not a:
			return b[k]
		if not b:
			return a[k]
		ia, ib = len(a) // 2 , len(b) // 2
		ma, mb = a[ia], b[ib]
		
		# when k is bigger than the sum of a and b's median indices 
		if ia + ib < k:
			# if a's median is bigger than b's, b's first half doesn't include k
			if ma > mb:
				return self.kth(a, b[ib + 1:], k - ib - 1)
			else:
				return self.kth(a[ia + 1:], b, k - ia - 1)
		# when k is smaller than the sum of a and b's indices
		else:
			# if a's median is bigger than b's, a's second half doesn't include k
			if ma > mb:
				return self.kth(a[:ia], b, k)
			else:
				return self.kth(a, b[:ib], k)



nums1, nums2 = [1,2], [3,4]

sl = Solution()
print( sl.findMedianSortedArrays( nums1, nums2 ) )



