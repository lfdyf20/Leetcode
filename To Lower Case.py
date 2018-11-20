class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return "".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in str)
       



str = "LOVELY"
sl = Solution()
print( sl.toLowerCase( str ) )