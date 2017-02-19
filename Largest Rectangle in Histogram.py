class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = []
        maxRes = 0
        for i in range( len(heights) ):
        	if stack and heights[i] < heights[stack[-1]]:
        		while stack and heights[i] <= heights[stack[-1]]:
        			h = heights[stack.pop()]
        			width = i if not stack else i-stack[-1]-1
        			maxRes = max( maxRes, h*width )
        	stack.append(i)
        heights.pop()
        return maxRes

        			




heights = [2,1,5,6,2,3]

sl = Solution()
print( sl.largestRectangleArea( heights ) )

# https://discuss.leetcode.com/topic/7599/o-n-stack-based-java-solution/16