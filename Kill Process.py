class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """ too slow
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        visited = [kill]
        res = []
        for i in visited:
        	res.append(i)
        	for pi in range(len(ppid)):
        		if ppid[pi] == i:
        			visited += [ pid[pi] ]
        return res


    def online(self, pid, ppid, kill):
    	dict = {}
    	for i, p in zip(pid, ppid):
    		if p in dict:
    			dict[p].append(i)
    		else:
    			dict[p] = [i]
    	to = [kill]
    	for i in to:
    		to.extend(dict.get(i, []))
    	return to




pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5

sl = Solution()
print( sl.killProcess( pid, ppid, kill ) )