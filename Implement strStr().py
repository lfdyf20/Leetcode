class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)):
            for j in range(len(needle)+1):
                if j == len(needle):
                    return i
                if i + j == len(haystack):
                    return -1
                if haystack[i+j] != needle[j]:
                    break

                





haystack, needle = "123445", "34"
sl = Solution()
print( sl.strStr(haystack, needle) )