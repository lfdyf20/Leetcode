import collections
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid( s ):
            ct = 0
            for i in s:
                if i == "(":
                    ct += 1
                    continue
                if i == ")":
                    ct -= 1
                    if ct < 0:
                        return False
            return ct == 0
            
        visited = set( [s] )
        res = []
        queue = collections.deque([s])
        done = False
        while queue:
        	t = queue.popleft()
        	if isValid( t ):
        		done = True
        		res.append( t )
        	if done:
        		continue
        	for x in range( len(t) ):
        		if t[x] not in ["(", ")"]:
        			continue
        		nt = t[:x] + t[x+1:]
        		if nt not in visited:
        			visited.add( nt )
        			queue.append( nt )
        return res




s = "(a)())()"

sl = Solution()
print( sl.removeInvalidParentheses( s ) )