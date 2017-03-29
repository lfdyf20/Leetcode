class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(s, k, path, res):
        	print(path, s)
        	if len(s)>3*k:
        		return
        	if len(s)<k:
        		return
        	if not s:
        		if k == 0:
        			res.append( path[:-1] )
        		return
        	dfs( s[1:], k-1, path+s[0]+'.', res )
        	if s[0] == '0':
        		return
        	if len(s)>=2:
        		dfs( s[2:], k-1, path+s[:2]+'.', res)
        	if len(s)>2 and int(s[:3])<=255:
        		dfs( s[3:], k-1, path+s[:3]+'.', res ) 

        res = []
        dfs( s, 4,'', res )
        return res


s = "25525511135"

sl = Solution()
print( sl.restoreIpAddresses( s ) )