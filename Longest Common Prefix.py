class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """ 
        def commonPrefix(s1, s2):
            i = 0
            print s1, s2

            for a, b in zip(s1,s2):
                if a != b:
                    break 
                i += 1
            return s1[:i]
        return "" if len(strs)==0 else reduce(commonPrefix, strs)






strs = ["abcd", "abd", "abcd" ]

sample = Solution()

print sample.longestCommonPrefix(strs)