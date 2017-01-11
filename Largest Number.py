class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        r = ''.join(sorted(map(str, nums), lambda x, y: [1, -1][x + y > y + x]))
        return r.lstrip('0') or '0'

    # def ln( self, nums ):

    # 	def compare(a , b):
    # 		if a+b > b+a:
    # 			return 1
    # 		else:
    # 			return -1
    # 	nums = [ str(num) for num in nums ]
    # 	nums = sorted(nums, key=compare)
    # 	print(nums)








nums = [3, 30, 34, 5, 9]
sl = Solution()
print( sl.largestNumber(nums) )
# print( sl.ln(nums) )