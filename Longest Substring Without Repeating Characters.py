class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        rec, res, start = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in rec:
                res = max(res, i-start)
                start = max(rec[ch]+1,start)
            rec[ch] = i
            # print(start, res)
        return max(res, len(s)-start)




s = "aab"
s = "abcabcbb"
s = "bbbbb"
s = "pwwkew"
s = "abba"


sl = Solution()
print( sl.lengthOfLongestSubstring( s ) )