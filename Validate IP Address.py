class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """

        def isIPv4(s):
        	try:
        		return str(int(s)) == s and 0 <= int(s) <= 255
        	except:
        		return False

        def isIPv6(s):
        	if len(s) > 4:
        		return False
        	try:
        		return int(s, 16) >= 0 and s[0] != '-'
        	except:
        		return False

        if IP.count(".") == 3 and all(isIPv4(x) for x in IP.split(".")):
        	return "IPv4"
        if IP.count(":") == 7 and all(isIPv6(x) for x in IP.split(":")):
        	return "IPv6"
        return "Neither"

        



IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"

sl = Solution()
print( sl.validIPAddress( IP ) )